from colorama import Fore, Style
from ..exceptions import InputBotExseption

def input_error(error):
    """Decorator takes an error message and return the error"""
    def error_handler(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, IndexError):
                print(Fore.RED + error + Style.RESET_ALL)
        return inner
    return error_handler

def confirm_prompt(message="Please confirm"):
    def handler(func):
        def inner(*args, **kwargs):
            user_input = input(f"{message} (yes/no) ")
            user_input = user_input.strip().lower()

            if user_input in ["yes", "y"]:
                return func(*args, **kwargs)
        return inner
    return handler

__all__ = ["input_error", "confirm_prompt"]
