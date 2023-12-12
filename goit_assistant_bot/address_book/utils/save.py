import pickle
from colorama import Fore, Style


def save_address_book(book, force_save=False):
    if book.is_dirty or force_save:
        dump_file = book.get_dump_file()
        if dump_file:
            with open(dump_file, "wb") as fh:
                book.is_dirty = False
                pickle.dump(book, fh)
                print(
                    Fore.LIGHTBLACK_EX + "\u2713 Contact book saved!" + Style.RESET_ALL
                )
        else:
            print(
                Fore.RED
                + "A dump file to save data is not specified."
                + Style.RESET_ALL
            )
    else:
        print(Fore.LIGHTBLACK_EX + "No updates to save." + Style.RESET_ALL)


__all__ = ["save_address_book"]
