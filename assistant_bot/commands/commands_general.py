from ..constants import MENU, TEXT


def show_menu():
    return MENU

def show_bye():
    return TEXT["BYE"]

def show_hello():
    return TEXT["GREETING"]


__all__ = [
    "show_hello",
    "show_menu",
    "show_bye",
]
