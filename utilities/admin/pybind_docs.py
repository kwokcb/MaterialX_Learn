import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path

# Path to Doxygen XML output
DOXYGEN_XML_DIR = Path("build/documents/doxygen_xml")

# Path to PyMaterialX bindings
PYBIND_DIR = Path("source/PyMaterialX")

# Map C++ qualified names → docstring text
doc_map = {}

def extract_docs_from_xml():
    """
    Parse Doxygen XML files and collect documentation for each function.
    Produces entries like:
      doc_map["MaterialX::Document::addNodeDefFromGraph"] = "...docstring..."
    """
    for xml_file in DOXYGEN_XML_DIR.glob("*.xml"):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall(".//memberdef[@kind='function']"):
            name = member.findtext("name") or ""
            qualified = member.findtext("qualifiedname") or ""

            # Handle stripping out <ref from:
            # <briefdescription>
            # <para>Create a <ref refid="class_node_def" kindref="compound">NodeDef</ref> and Functional Graph based on a Compound <ref refid="class_node_graph" kindref="compound">NodeGraph</ref>. </para>
            # </briefdescription>
            member_brief_elem = member.find("briefdescription//para")
            # Remove <ref> and </ref> tags but keep their text
            result = []
            if member_brief_elem is not None:
                for elem in member_brief_elem.iter():
                    if elem.tag == "ref":
                        if elem.text:
                            result.append(elem.text)
                        if elem.tail:
                            result.append(elem.tail)
                    elif elem is member_brief_elem:
                        if elem.text:
                            result.append(elem.text)
            brief = "".join(result).strip()

            #brief = (member.findtext("briefdescription//para") or "").strip()
            #brief = (member.findtext("briefdescription//para") or "").strip()

            # Extract detailed paragraphs not including <parameterlist> or <simplesect>
            detail_parts = []
            for para in member.findall("detaileddescription/para"):
                if para.find("parameterlist") is None and para.find("simplesect") is None:
                    detail_parts.append("".join(para.itertext()).strip())
            detail = "\n".join(p for p in detail_parts if p)

            # Extract parameter docs
            params = []
            for param_item in member.findall(".//parameterlist[@kind='param']/parameteritem"):
                pname = param_item.findtext("parameternamelist/parametername")
                pdesc = "".join(param_item.find("parameterdescription").itertext()).strip()
                if pname and pdesc:
                    params.append(f"    {pname}: {pdesc}")

            # Extract return doc
            ret = None
            retsect = member.find(".//simplesect[@kind='return']")
            if retsect is not None:
                ret = "".join(retsect.itertext()).strip()

            # Combine into a single docstring
            doc_parts = []
            if brief:
                doc_parts.append(brief)
            if detail:
                doc_parts.append(detail)
            if params:
                doc_parts.append("Args:\n" + "\n".join(params))
            if ret:
                doc_parts.append(f"Returns:\n    {ret}")

            full_doc = "\n\n".join(doc_parts).strip()

            if full_doc and len(qualified) > 0:
                if qualified == "Document::addNodeDefFromGraph":
                    print("Document::addNodeDefFromGraph", full_doc)
                    print(member.find("briefdescription"))

                # Normalize qualified name to include namespace
                if not qualified.startswith("MaterialX::"):
                    qualified = "MaterialX::" + qualified

                doc_map[qualified] = full_doc

def extract_docs_from_xml_old():
    for xml_file in DOXYGEN_XML_DIR.glob("*.xml"):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall(".//memberdef[@kind='function']"):
            name = member.findtext("name")
            qualified = member.findtext("qualifiedname")            
            brief = (member.findtext("briefdescription//para") or "").strip()
            detail = (member.findtext("detaileddescription//para") or "").strip()
            full_doc = (brief + "\n\n" + detail).strip()
            if full_doc:
                if qualified == "Document::addNodeDefFromGraph":
                    print("Document::addNodeDefFromGraph", full_doc)
                doc_map[qualified] = full_doc

def find_and_insert_docs():
    cpp_files = list(PYBIND_DIR.rglob("*.cpp"))

    for cpp in cpp_files:
        text = cpp.read_text(encoding="utf-8")

        # Regex for pybind11 .def lines
        pattern = re.compile(r'\.def\(\s*"([^"]+)"\s*,\s*&([A-Za-z0-9_:]+)')
        changed = False
        new_lines = []

        for line in text.splitlines():
            m = pattern.search(line)
            if m:
                py_name = m.group(1)
                cpp_ref = m.group(2)
                # Example: MaterialX::Node::createInput
                doc = doc_map.get(cpp_ref)
                if doc and 'DOC' not in line:
                    # Escape quotes and newlines
                    escaped = doc.replace('"', '\\"').replace('\n', '\\n')
                    # Add a docstring parameter
                    if line.strip().endswith(")"):
                        line = line.rstrip(")") + f', "{escaped}")'
                    else:
                        line += f', "{escaped}"'
                    changed = True
            new_lines.append(line)

        if changed:
            cpp.write_text("\n".join(new_lines), encoding="utf-8")
            print(f"Updated docstrings in {cpp}")

def main():
    extract_docs_from_xml()
    # Write doc_mape to files for debugging
    json_path = Path("doc_map.json")
    import json
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(doc_map, f, indent=2)

    #find_and_insert_docs()
    print(f"Injected {len(doc_map)} doc entries.")

if __name__ == "__main__":
    main()
