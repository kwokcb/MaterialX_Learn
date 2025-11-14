"""
@file mx_test_grid.py
@brief Generate a Markdown grid summarizing GitHub Actions jobs from a YAML file.
"""
import os
try:
    import yaml
except ImportError:
    raise ImportError("PyYAML is required to run this script. Please install it via 'pip install pyyaml'.")
import argparse

class MaterialXTestGridGenerator:

    def load_yaml(self, yaml_file_path):
        """
        Load YAML file from the given path.
        @param yaml_file_path: Path to the YAML file.
        @return: Parsed YAML data or None if file not found.
        """
        if not yaml_file_path:
            print("No YAML file path provided. Using default path.")
            return None
        if not os.path.isfile(yaml_file_path):
            print(f"YAML file not found at {yaml_file_path}. Please provide a valid path.")
            return None
        with open(yaml_file_path, 'r') as file:
            return yaml.safe_load(file)

    def create_step_line(self, step):
        """
        @brief Create a single line description for a step.
        @param step: Step dictionary from YAML.
        @return: Formatted step description string.
        """

        ifstatement = step.get('if', '')
        if len(ifstatement):
            # If "matrix.<string>"" is used, we cannot parse it here
            # remove "matrix." and replace <string> with *<string>*
            if 'matrix.' in ifstatement:
                parts = ifstatement.split('matrix.')
                for i in range(1, len(parts)):
                    subparts = parts[i].split()
                    subparts[0] = '*' + subparts[0] + '*'
                    parts[i] = ' '.join(subparts)
                ifstatement = ''.join(parts)
            if_string = 'If (' + ifstatement + ')'
            step_string = f"{if_string}\n    - {step.get('name', 'Unnamed Step')}"
        else:
            step_string = f"{step.get('name', 'Unnamed Step')}"

        result = step_string
        return result

    def create_step_description(self, jobs):
        """
        @brief Create step descriptions for each job.
        @param jobs: Jobs dictionary from YAML.
        @return: Formatted step descriptions string.
        """

        runner_os = [ { 'os': 'Linux', 'steps': [] }, 
                    {  'os': 'Windows', 'steps': [] },
                    { 'os' : 'macOS', 'steps': [] } ]

        result = ''
        for job_name, job_details in jobs: 
            step_list = []
            name = job_details.get('name', job_name)
            if name:
                job_name = name
            result += f"## Steps For Job: `{job_name}`\n"
            steps = job_details.get('steps', [])
            for idx, step in enumerate(steps, start=1):
                step_list.append(f"{self.create_step_line(step)}")
    
            # Split into 3 lists. One per os
            if job_name == 'build':
                result += "<table>\n"
                result += "<tr>\n"
                result += "<th>Linux Steps</th>\n"
                result += "<th>Windows Steps</th>\n"
                result += "<th>macOS Steps</th>\n"
                result += "</tr>\n"

                result += "<tr>\n"

                linux_list = step_list
                # Strip out anything that has 'runner.os == 'Windows' or 
                # 'runner.os == 'macOS'
                linux_list = [step for step in step_list if 'runner.os' not in step or 'Linux' in step]
                #result += "### Linux Steps\n"
                result += "<td><ol>"
                for step in linux_list:
                    result += f"<li>{step}\n"

                wndows_list = step_list
                windows_list = [step for step in step_list if 'runner.os' not in step or 'Windows' in step]
                #result += "\n### Windows Steps\n"
                result += "</ol><td><ol>"
                for step in windows_list:
                    result += f"<li>{step}\n"

                macos_list = step_list
                macos_list = [step for step in step_list if 'runner.os' not in step or 'macOS' in step]
                #result += "\n### macOS Steps\n"
                result += "<td><ol>"
                for step in macos_list:
                    result += f"<li>{step}\n"
                result += "</tr>\n"
                result += "</table>\n\n"

            else:
                result += "<ol>\n"
                for step in step_list:
                    result += '<li>' + step + '\n'
                result += "</ol>\n\n"
        return result
        
    def create_table(self, jobs):
        """
        @brief Create a Markdown table summarizing the jobs.
        @param jobs: Jobs dictionary from YAML.
        @return: Formatted Markdown table string.
        """
        if not jobs:
            return ""


        # Iterate through jobs and extract relevant information
        total_grid = ""
        for job_name, job_details in jobs:
            markdown_grid = ""
            if job_name == 'wheels':
                continue  # Skip the 'wheels' job
            if 'strategy' in job_details and 'matrix' in job_details['strategy']:
                matrix = job_details['strategy']['matrix']
                if 'include' in matrix:
                    for job in matrix['include']:
                        name = job.get('name', job_name)
                        osystem = job.get('os', 'Unspecified')
                        architecture = job.get('architecture', '')
                        osystem = osystem + ' ' + architecture if architecture != 'N/A' else os
                        compiler = job.get('compiler', 'Default')
                        compiler_version = job.get('compiler_version', '')
                        python = job.get('python', '')
                        cmake_config = job.get('cmake_config', 'None')
                        
                        # Collect additional configuration
                        additional_config = ', '.join([key for key in job.keys() if key not in ['name', 'os', 'architecture', 'compiler', 'compiler_version', 'python', 'cmake_config']])
                        
                        # Collect test flags
                        test_flags = []
                        if 'test_shaders' in job and job['test_shaders'] == 'ON':
                            test_flags.append('test_shaders')
                        if 'coverage_analysis' in job and job['coverage_analysis'] == 'ON':
                            test_flags.append('coverage_analysis')
                        if 'static_analysis' in job and job['static_analysis'] == 'ON':
                            test_flags.append('static_analysis')
                        if 'test_render' in job and job['test_render'] == 'ON':
                            test_flags.append('test_render')

                        # Join test flags into a string
                        test_flags_str = ', '.join(test_flags) if test_flags else 'N/A'
                        
                        markdown_line = f"| {name} | {osystem} | {compiler}, {compiler_version} | {python} | {cmake_config} | {additional_config} |\n"
                        markdown_grid += markdown_line
                else:
                    # Handle cases where 'include' is not present
                    markdown_grid += f"| {job_name} | N/A | N/A | N/A | N/A | N/A |\n"

            if len(markdown_grid) > 0:
                header = f"## Workflow Matrix for {job_name}\n\n"
                header += "| Workflow Name | OS | Compiler | Python | Build Flags | Test Flags |\n"
                header += "|----------|----|----------|--------|-------------------|------------|\n"
                markdown_grid = header + markdown_grid

            total_grid += markdown_grid + "\n"    
        
        return total_grid


def main():

    parser = argparse.ArgumentParser(description="Generate Markdown grid from MaterialX GitHub Actions YAML")
    parser.add_argument('yaml_file', help='Path to the GitHub Actions YAML file')
    parser.add_argument('-o', '--output', help='Path to output Markdown file', default=None)  
    args = parser.parse_args()

    yaml_file_path = args.yaml_file if args.yaml_file else ''

    generator = MaterialXTestGridGenerator()
    data = generator.load_yaml(yaml_file_path)
    if not data:
        return(-1)
    
    jobs = data['jobs'].items()
    if not jobs:
        print("No jobs found in the YAML file.")
        return(-1)

    # Build Markdown grid and step descriptions
    markdown_grid = generator.create_table(jobs)
    steps = generator.create_step_description(jobs)

    result = ''
    if markdown_grid:
        result += markdown_grid
    if steps:
        result += '\n\n' + steps

    if result:
        if args.output:
            with open(args.output, 'w') as output_file:
                output_file.write(result)
        else:
            print(result)
    else:
        print("No jobs found in the YAML file.")


if __name__ == "__main__":
    main()
