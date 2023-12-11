from colorama import Style, Fore


def print_diff(old_value, new_value):
    print(
        Style.DIM
        + old_value
        + Style.RESET_ALL
        + Fore.BLUE
        + " => "
        + new_value
        + Style.RESET_ALL
    )


__all__ = [
    "print_diff",
]
