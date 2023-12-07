from colorama import Style

def print_diff(old_value, new_value):
    print(Style.DIM + old_value + Style.RESET_ALL + f" / {new_value}")


__all__ = [
    "print_diff",
]
