from colorama import Fore, Style
from ..constants import TEXT
from .commands import COMMANDS, ARGUMET_TYPES, VALIDATION_RULES

def print_rules(rules=None):
    if not rules:
        rules = VALIDATION_RULES

    print(Fore.YELLOW + "Validation rules:" + Style.RESET_ALL)
    for k, v in rules.items():
        print(f"{k:<30} - {v}")

def print_argument_types(types=None):
    if not types:
        types = ARGUMET_TYPES

    print(Fore.YELLOW + "Types of argumets:" + Style.RESET_ALL)
    for k, v in types.items():
        print(f"{k:<30} - {v}")

def show_help(args, *_):
    """Displays help information"""
    cmd = str(args[0]).strip().lower() if len(args) > 0 else None
    output = ""
    
    cmd_found = False
    for command in COMMANDS:
        commands = command["commands"]
        commands_string = " | ".join(commands)
        arguments_string = f" {" ".join(command["arguments"])}" if len(command["arguments"]) > 0 else ""
        description = command["description"]
        if cmd:
            if cmd in commands:
                cmd_found = True
                rules = command.get("rules", None)
                description += f": {Fore.GREEN + commands[0] + Style.RESET_ALL}{Fore.BLUE + arguments_string + Style.RESET_ALL}"
                output += f"{Fore.GREEN + commands_string + Style.RESET_ALL}\n- {description}\n"
                print(output)

                if rules:
                    print_rules(rules)
                    break
        else:
            description += f": {commands[0]}{arguments_string}"
            output += f"{commands_string:<30} - {description}\n"

    if cmd:
        if not cmd_found:
            print(Fore.LIGHTBLACK_EX + f"\"{cmd}\" not found, type \"help\" to see all commands" + Style.RESET_ALL)
    else:
        print(output)
        print_argument_types(ARGUMET_TYPES)
        print()
        print_rules(VALIDATION_RULES)

def show_bye(*_):
    print(TEXT["BYE"])

def show_hello(*_):
    print(TEXT["GREETING"])


__all__ = [
    "show_hello",
    "show_help",
    "show_bye",
]
