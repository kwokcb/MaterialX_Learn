#!/usr/bin/env python3
"""
mxcmd.py — MaterialX command runner

Usage:
  python mxcmd.py -l
  python mxcmd.py <command> [command-args ...]
"""

import sys
from importlib.metadata import entry_points

class MaterialXCommandRunner:

    def __init__(self) -> None:
        self.ENTRYPOINT_GROUP = "console_scripts"
        self.PACKAGE_PREFIX = "MaterialX."
        self.ep = None

    def find_materialx_commands(self) -> dict:
        """
        Find all MaterialX commands registered as entry points.
        Returns:
            Dictionary mapping command names to entry points.
        """
        commands = {}
        self.eps = entry_points().select(group=self.ENTRYPOINT_GROUP)
        for ep in self.eps:
            if ep.value.startswith(self.PACKAGE_PREFIX):
                commands[ep.name] = ep
        return commands


    def list_commands(self, commands: dict) -> None:
        """
        Print a list of available commands.

        @param commands: Dictionary of available commands
        """
        print("Available MaterialX commands:")
        for name in sorted(commands):
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

    def parse_args(self, argv : list, commands: dict) -> tuple[bool, str, list[str]]:
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

        if command not in commands:
            print(f"Unknown command: {command}")
            return False, "", []

        return False, command, command_args


    def run_command(self, command : str, command_args : list, commands: dict) -> str:
        """
        Load and run the specified command.

        @param command: Name of the command to run
        @param command_args: List of arguments to pass to the command
        @param commands: Dictionary of available commands
        """
        ep = commands[command]

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
    commands = runner.find_materialx_commands()
    argv = sys.argv[1:]

    list_only, command, command_args = runner.parse_args(argv, commands)

    # Just list commands
    if list_only:
        runner.list_commands(commands)
        return

    # Run the specified command
    if command:
        result = runner.run_command(command, command_args, commands)
        if result:
            print(result, file=sys.stderr)  
    
if __name__ == "__main__":
    main()
