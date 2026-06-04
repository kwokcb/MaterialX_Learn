"""
XML Compliance Checker for MaterialX (.mtlx) files
"""

import os
import sys
import argparse
from xml.etree import ElementTree as ET
import re

class XMLComplianceChecker:
    """
    @brief Checks XML compliance of .mtlx files and reports errors with line numbers and content.    
    """
    def __init__(self):
        """
        @brief Initializes the XMLComplianceChecker with an empty error list.
        """
        self.errors = []
    
    def check_file(self, filepath):
        """
        @brief Checks the XML compliance of a single file and records any errors found.
        @param filepath The path to the file to check.
        @return True if the file is compliant, False otherwise.
        """
        self.errors = []
        
        if not os.path.exists(filepath):
            self.errors.append({
                'file': filepath,
                'line': None,
                'message': f"File not found"
            })
            return False
        
        try:
            ET.parse(filepath)
            return True
        except ET.ParseError as e:
            error_msg = str(e)
            line_num = self._get_line_number(error_msg)
            
            # Get the actual line from the file
            line_content = None
            if line_num:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    if line_num <= len(lines):
                        line_content = lines[line_num - 1].rstrip('\n\r')
            
            self.errors.append({
                'file': filepath,
                'line': line_num,
                'line_content': line_content,
                'message': error_msg
            })
            return False
    
    def _get_line_number(self, error_msg):
        """
        @brief Extracts the line number from an XML parsing error message.
        @param error_msg The error message from which to extract the line number.
        @return The line number if found, None otherwise.
        """
        match = re.search(r'line\s+(\d+)', error_msg, re.IGNORECASE)
        return int(match.group(1)) if match else None


def main():
    """
    @brief Command to check XML compliance of MateraiLX files. 
    @param path The file or folder path to check for .mtlx files.
    @return Exits with code 0 if compliant, 1 if errors are found.
    """
    parser = argparse.ArgumentParser(description='Check XML compliance of .mtlx files')
    parser.add_argument('path', help='File or folder path')
    args = parser.parse_args()
    
    # Find all .mtlx files
    files = []
    if os.path.isfile(args.path) and args.path.endswith('.mtlx'):
        files = [args.path]
    elif os.path.isdir(args.path):
        for root, _, filenames in os.walk(args.path):
            files.extend(os.path.join(root, f) for f in filenames if f.endswith('.mtlx'))
    
    # Check each file
    checker = XMLComplianceChecker()
    errors_found = False
    
    for filepath in files:
        if not checker.check_file(filepath):
            print(f"* Error(s) found in file: {filepath}")
            errors_found = True
            for err in checker.errors:
                if err['line']:
                    print(f"   * Line {err['line']}: {err['message']}")
                    if err['line_content']:
                        print(f"   * {err['line_content']}")
                else:
                    print(f"   * {err['message']}")
    
    sys.exit(1 if errors_found else 0)

if __name__ == "__main__":
    main()
