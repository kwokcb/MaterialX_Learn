import sys
import json
import argparse

def md_table(headers, rows):
    """
    Create a Markdown table.
    headers: list of strings
    rows: list of list of strings
    """
    md = "| " + " | ".join(headers) + " |\n"
    md += "| " + " | ".join(["---"]*len(headers)) + " |\n"
    for row in rows:
        md += "| " + " | ".join(str(cell) for cell in row) + " |\n"
    return md + "\n"

def json_to_markdown(data):
    md = "# MaterialX Library Comparison\n\n"

    # --- Node Definitions ---
    nodeDefs = data.get("nodeDefs", {})

    for section_name, nodes in [("added", nodeDefs.get("added", [])),
                                ("removed", nodeDefs.get("removed", [])),
                                ("modified", nodeDefs.get("modified", []))]:
        if not nodes:
            continue
        md += f"## {section_name.capitalize()} Node Definitions ({len(nodes)})\n\n"
        headers = ["Name", "Category", "Node Group", "Type"]
        if section_name == "modified":
            headers.append("Differences")
        rows = []
        for n in nodes:
            row = [n.get("name", ""), n.get("category", ""), n.get("group", ""), n.get("type", "")]
            if section_name == "modified":
                diffs = n.get("differences", [])
                row.append("<br>".join(diffs))
            rows.append(row)
        md += md_table(headers, rows)

    # --- Shader Targets ---
    targets = data.get("targets", {})
    md += "## Shader Targets\n\n"
    firstTargets = targets.get("first", [])
    secondTargets = targets.get("second", [])
    addedTargets = targets.get("added", [])
    md += f"- First library targets ({len(firstTargets)}): {', '.join(firstTargets)}\n"
    md += f"- Second library targets ({len(secondTargets)}): {', '.join(secondTargets)}\n"
    if addedTargets:
        md += f"- Added targets: {', '.join(addedTargets)}\n"
    md += "\n"

    # --- Implementations ---
    impls = data.get("implementations", {})

    for section_name, items in [("added", impls.get("added", [])),
                                ("removed", impls.get("removed", [])),
                                ("modified", impls.get("modified", []))]:
        if not items:
            continue
        md += f"## {section_name.capitalize()} Implementations ({len(items)})\n\n"
        headers = ["Name", "Node String", "Type", "Source"]
        if section_name == "modified":
            headers.append("Differences")
        rows = []
        for i in items:
            row = [i.get("name", ""), i.get("nodeString", ""), i.get("type", ""), i.get("source", "")]
            if section_name == "modified":
                diffs = i.get("differences", [])
                row.append("<br>".join(diffs))
            rows.append(row)
        md += md_table(headers, rows)

    return md

def main():
    parser = argparse.ArgumentParser(description="Convert MaterialX JSON comparison to Markdown")
    parser.add_argument("json_file", help="Input JSON file")
    parser.add_argument("--out", help="Output Markdown file", default=None)
    opts = parser.parse_args()

    with open(opts.json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    md = json_to_markdown(data)

    if opts.out:
        with open(opts.out, "w", encoding="utf-8") as f:
            f.write(md)
    else:
        print(md)

if __name__ == "__main__":
    main()
