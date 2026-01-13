#!/usr/bin/env python3
"""
mxcmd.py — MaterialX command runner

Usage:
  python mxcmd.py -l
  python mxcmd.py <command> [command-args ...]
"""

import sys
from importlib.metadata import entry_points

ENTRYPOINT_GROUP = "console_scripts"
PACKAGE_PREFIX = "MaterialX."

def find_materialx_commands() -> dict[str, object]:
    """
    Find all MaterialX commands registered as entry points.
    Returns:
        Dictionary mapping command names to entry points.
    """
    commands = {}
    eps = entry_points().select(group=ENTRYPOINT_GROUP)
    for ep in eps:
        if ep.value.startswith(PACKAGE_PREFIX):
            commands[ep.name] = ep
    return commands


def list_commands(commands) -> None:
    """
    Print a list of available commands.

    @param commands: Dictionary of available commands
    """
    print("Available MaterialX commands:")
    for name in sorted(commands):
        print(f"  {name}")

def help() -> None:
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
    sys.exit(1)


def parse_args(argv, commands) -> tuple[bool, str | None, list[str]]:
    """
    Determine if we are listing or running a command.

    @param argv: List of command-line arguments (excluding script name)
    @param commands: Dictionary of available commands
    @return: 
        True, None, [] if listing commands
        False, command name, command arguments if running a command
    """
    if not argv or argv[0] in ("-h", "--help"):
        help()

    if argv[0] in ("-l", "--list"):
        return True, None, []

    # Treat first argument as command name
    command = argv[0]
    command_args = argv[1:]

    if command not in commands:
        print(f"Unknown command: {command}", file=sys.stderr)
        help()

    return False, command, command_args


def run_command(command, command_args, commands) -> None:
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
        print(f"Failed to load command '{command}': {e}", file=sys.stderr)
        sys.exit(1)

    # Rebuild argv for the command
    sys.argv = [command] + command_args

    try:
        func()
    except SystemExit as e:
        if e.code not in (None, 0):
            sys.exit(e.code)


def main():
    """
    Main entry point for the MaterialX command runner.
    """
    commands = find_materialx_commands()
    argv = sys.argv[1:]

    list_only, command, command_args = parse_args(argv, commands)

    # Just list commands
    if list_only:
        list_commands(commands)
        return

    # Run the specified command
    run_command(command, command_args, commands)

if __name__ == "__main__":
    main()
