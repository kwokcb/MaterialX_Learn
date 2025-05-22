import ast
import sys
from typing import List, Dict


class ArgparseInspector(ast.NodeVisitor):
    def __init__(self):
        self.arguments: List[Dict[str, str]] = []

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute) and node.func.attr == 'add_argument':
            argument = {
                "options": [],
                "dest": "",
                "help": "",
                "type": "",
                "default": "",
                "action": ""
            }

            # Positional and optional options
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    argument["options"].append(arg.value)
                elif isinstance(arg, ast.List):
                    argument["options"].extend([
                        elt.value for elt in arg.elts
                        if isinstance(elt, ast.Constant) and isinstance(elt.value, str)
                    ])

            for kw in node.keywords:
                if kw.arg == 'help' and isinstance(kw.value, ast.Constant):
                    argument["help"] = kw.value.value
                elif kw.arg == 'dest' and isinstance(kw.value, ast.Constant):
                    argument["dest"] = kw.value.value
                elif kw.arg == 'type':
                    if isinstance(kw.value, ast.Name):
                        argument["type"] = kw.value.id
                    elif isinstance(kw.value, ast.Attribute):
                        names = []
                        current = kw.value
                        while isinstance(current, ast.Attribute):
                            names.insert(0, current.attr)
                            current = current.value
                        if isinstance(current, ast.Name):
                            names.insert(0, current.id)
                        argument["type"] = ".".join(names)
                elif kw.arg == 'default':
                    if isinstance(kw.value, ast.Constant):
                        argument["default"] = repr(kw.value.value)
                elif kw.arg == 'action':
                    if isinstance(kw.value, ast.Constant):
                        argument["action"] = kw.value.value

            # Normalize type based on action
            action = argument["action"]
            base_type = argument["type"]

            if action in ("store_true", "store_false"):
                argument["type"] = "bool"
            elif action == "append":
                argument["type"] = f"list of {base_type or 'string'}"
            elif not base_type:
                argument["type"] = "string"  # default type

            self.arguments.append(argument)

        self.generic_visit(node)


def extract_args_from_file(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source, filename)
    inspector = ArgparseInspector()
    inspector.visit(tree)

    return inspector.arguments


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python getcmd.py <target_script.py>")
        sys.exit(1)

    script_path = sys.argv[1]
    try:
        args_info = extract_args_from_file(script_path)
        command = script_path.split("/")[-1].split(".")[0]
        print(f"Command: {command}\n")
        if not args_info:
            print("Has no arguments")
        else:
            for arg in args_info:
                options = ", ".join(arg["options"]) or "(required)"
                dest = arg["dest"] or "(auto)"
                help_text = arg["help"]
                type_info = f"Type: {arg['type']}."
                default_info = f"Default: {arg['default']}." if arg["default"] else ""

                if options == "(required)":
                    print(f"{dest:20} Required: {help_text} {type_info} {default_info}")
                else:
                    print(f"{options:20} Optional: {help_text} {type_info} {default_info}")
    except Exception as e:
        print(f"Error: {e}")
