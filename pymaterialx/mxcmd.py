#!/usr/bin/env python3
"""
mxcmd.py — MaterialX command runner

Usage:
  python mxcmd.py -l
  python mxcmd.py <command> [command-args ...]
"""

import sys
#from importlib.metadata imporett entry_points
import importlib.metadata as importlib_metadata

class MaterialXCommandRunner:

    def __init__(self) -> None:
        self.ENTRYPOINT_GROUP = "console_scripts"   # Entry point group for commands
        self.PACKAGE = "MaterialX"                  # MaterialX package name
        self.PACKAGE_PREFIX = f"{self.PACKAGE}."    # Module prefix for MaterialX
        self.ep = None
        self.commands = {}

    def get_commands(self) -> dict | None:
        """
        Get the available MaterialX commands.
        """
        if not self.commands:
            self._cache_commands()
        return self.commands

    def _cache_commands(self):
        """
        Find all MaterialX commands registered as entry points.
        """
        self.commands = {}

        scan_distributions = False
        # Scan distributions for MaterialX entry points
        if scan_distributions:
            for dist in importlib_metadata.distributions():
                if dist.metadata["Name"] == self.PACKAGE:
                    for ep in dist.entry_points:
                        if ep.group == self.ENTRYPOINT_GROUP:
                            self.commands[ep.name] = ep
                    break
        # Scan all entry points for MaterialX commands
        else:
            self.eps = importlib_metadata.entry_points().select(group=self.ENTRYPOINT_GROUP)
            for ep in self.eps:
                if ep.value.startswith(self.PACKAGE_PREFIX):
                    self.commands[ep.name] = ep

    def list_commands(self) -> None:
        """
        Print available commands for the MaterialX package.

        @param commands: Dictionary of available commands
        @return: None
        """
        cmds = self.get_commands()
        if not cmds:
            print("No MaterialX commands found.")
            return

        try:
            version = importlib_metadata.version("MaterialX")
            version = f" v{version}"
        except importlib_metadata.PackageNotFoundError:
            version = ""
        print(f"MaterialX{version} commands:")
        for name in sorted(cmds):
            print(f"  {name}")

    def help(self) -> None:
        """
        Print help message.
        """
        print(
            "Run commands from MaterialX package.\n\n"
            "usage: mxcmd [options] <command> [command-args ...]\n\n"
            "positional arguments:\n"
            "  command         Command to run\n"
            "  command-args    Arguments for the command\n\n"
            "options:\n"
            "  -h, --help      Show this help message and exit\n"
            "  -l, --list      List available commands\n"
        )

    def parse_args(self, argv : list) -> tuple[bool, str, list[str]]:
        """
        Determine if we are listing or running a command.

        @param argv: List of command-line arguments (excluding script name)
        @param commands: Dictionary of available commands
        @return: 
            - True, "", [] if listing commands
            - False, "", [] if command is not found
            - False, command name, command arguments if command found to run
        """
        if not argv or argv[0] in ("-h", "--help"):
            self.help()
            return False, "", []

        if argv[0] in ("-l", "--list"):
            return True, "", []

        # Treat first argument as command name
        command = argv[0]
        command_args = argv[1:]

        cmds = self.get_commands()
        if command not in cmds:
            print(f"Unknown command: {command}")
            return False, "", []

        return False, command, command_args


    def run_command(self, command : str, command_args : list) -> str:
        """
        Load and run the specified command.

        @param command: Name of the command to run
        @param command_args: List of arguments to pass to the command
        @param commands: Dictionary of available commands
        """
        cmds = self.get_commands()
        if not cmds:
            return "No MaterialX commands found."
        
        ep = cmds[command]

        try:
            func = ep.load()
        except Exception as e:
            return f"Failed to load command '{command}'."                    

        # Rebuild argv for the command
        sys.argv = [command] + command_args

        try:
            func()
        except SystemExit as e:
            if e.code not in (None, 0):
                return f"Failed to load command '{command}'."                    
        
        return ""


def main():
    """
    Main entry point for the MaterialX command runner.
    """
    runner = MaterialXCommandRunner()
    argv = sys.argv[1:]

    list_only, command, command_args = runner.parse_args(argv)

    # Just list commands
    if list_only:
        runner.list_commands()
        return

    # Run the specified command
    if command:
        result = runner.run_command(command, command_args)
        if result:
            print(result, file=sys.stderr)  
    
if __name__ == "__main__":
    main()
