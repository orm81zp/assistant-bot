from colorama import Fore, Style

def input_error(error, use_colored_message=False):
    """The decorator checks ValueError, IndexError exceptions"""
    def error_handler(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, IndexError):
                if use_colored_message:
                    print(Fore.RED + error + Style.RESET_ALL)
                else:
                    print(error)
        return inner
    return error_handler

__all__ = ["input_error"]
