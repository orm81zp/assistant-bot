import unittest
import io
from unittest.mock import patch
from goit_assistant_bot.address_book.classes import AddressBook, Record


class TestTagCommands(unittest.TestCase):
    """Tests AddressBook class commands related to tags"""

    book: AddressBook

    def setUp(self):
        self.book = AddressBook()

    def test_init(self):
        """initial state."""


if __name__ == "__main__":
    unittest.main()
