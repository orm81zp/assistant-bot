from colorama import Fore, Style

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

__all__ = ["input_error"]
