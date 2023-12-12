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


def print_message(text):
    def get_name(name):
        print(
            Fore.LIGHTBLACK_EX
            + name.capitalize()
            + " "
            + text.lower()
            + Style.RESET_ALL
        )

    return get_name


__all__ = [
    "print_diff",
    "print_message",
]
