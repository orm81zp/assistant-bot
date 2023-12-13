import unittest
import io
from unittest.mock import patch, call
from goit_assistant_bot.address_book.classes import AddressBook
from goit_assistant_bot.address_book.exceptions import ValidationValueException
from goit_assistant_bot.exceptions import InputBotExseption, UnexpectedException
from goit_assistant_bot.bot import run_bot

book = AddressBook()


class TestBot(unittest.TestCase):
    """Tests Bot"""

    def setUp(self):
        pass

    @patch("goit_assistant_bot.bot.start_work", return_value=book)
    @patch(
        "goit_assistant_bot.bot.get_prompt_input",
        side_effect=["add-contact Max", "save", "exit"],
    )
    @patch(
        "goit_assistant_bot.bot.parse_input",
        side_effect=[
            ("add-contact", "func", ["Max"]),
            ("save", "func", []),
            ("exit", "func", []),
        ],
    )
    @patch("goit_assistant_bot.bot.commands_handler")
    @patch("goit_assistant_bot.bot.save")
    @patch("goit_assistant_bot.bot.stop_work")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_run_bot(
        self,
        mock_stdout,
        mock_stop_work,
        mock_save,
        mock_commands_handler,
        mock_parse_input,
        mock_get_prompt_input,
        mock_start_work,
    ):
        """Tests if all functions called"""
        run_bot()
        # Welcome message found
        self.assertIn("GoIT Assistant Bot!", mock_stdout.getvalue())
        # start_work called
        mock_start_work.assert_called_once()
        # get_prompt_input called
        mock_get_prompt_input.assert_called_with("Enter a command: ")
        # get_prompt_input called
        mock_parse_input.assert_has_calls(
            [call("add-contact Max"), call("save"), call("exit")]
        )
        # commands_handler called
        mock_commands_handler.assert_has_calls(
            [
                call(book, ["func", ["Max"]]),
                call(book, ["func", []]),
                call(book, ["func", []]),
            ]
        )
        # save called one
        mock_save.assert_called_once()
        # stop_work called after breaking the while loop by exit command
        mock_stop_work.assert_called_once()

    @patch("goit_assistant_bot.bot.start_work")
    @patch("goit_assistant_bot.bot.get_prompt_input")
    @patch(
        "goit_assistant_bot.bot.parse_input",
        side_effect=[
            (None, None, []),
            ("exit", None, []),
        ],
    )
    @patch("goit_assistant_bot.bot.commands_handler")
    @patch("goit_assistant_bot.bot.save")
    @patch("goit_assistant_bot.bot.stop_work")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_run_bot_no_command(self, mock_stdout, *_):
        """Tests message for empty command"""
        run_bot()
        # Welcome Invalid command found
        self.assertIn('Invalid command. Type "help"', mock_stdout.getvalue())

    @patch("goit_assistant_bot.bot.start_work")
    @patch("goit_assistant_bot.bot.get_prompt_input")
    @patch(
        "goit_assistant_bot.bot.parse_input",
        side_effect=[
            ("help", None, []),
            ("help", None, []),
            ("help", None, []),
            ("exit", None, []),
        ],
    )
    @patch(
        "goit_assistant_bot.bot.commands_handler",
        side_effect=[
            InputBotExseption,
            ValidationValueException("Validation Error!"),
            UnexpectedException("Unexpected Exception!"),
            None,
        ],
    )
    @patch("goit_assistant_bot.bot.save")
    @patch("goit_assistant_bot.bot.stop_work")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_run_bot_exceptions(self, mock_stdout, mock_stop_work, *_):
        """Tests exceptions"""
        run_bot()
        self.assertIn("Please, enter a command to begin.", mock_stdout.getvalue())
        self.assertIn("Validation Error!", mock_stdout.getvalue())
        self.assertIn("Unexpected Exception!", mock_stdout.getvalue())
        self.assertIn("Oops! Something went wrong!", mock_stdout.getvalue())
        mock_stop_work.assert_called_once()


if __name__ == "__main__":
    unittest.main()
