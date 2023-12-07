from ..constants import MENU, TEXT


def show_menu(*_):
    print(MENU)

def show_bye(*_):
    print(TEXT["BYE"])

def show_hello(*_):
    print(TEXT["GREETING"])


__all__ = [
    "show_hello",
    "show_menu",
    "show_bye",
]
