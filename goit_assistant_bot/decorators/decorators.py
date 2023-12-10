from colorama import Fore, Style

def input_error(error, use_colored_message=False):
    """
    This is a Decorator
    Validates for ValueError, IndexError exceptions and prints received error message if they are raised.

    Parameters:
        cmd (str): a command

    Returns: 
        error_handler (function): hendler of decorated function 
    """
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
