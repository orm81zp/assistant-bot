import unittest
from unittest.mock import patch, Mock
from goit_assistant_bot.address_book.classes import AddressBook
from goit_assistant_bot.exceptions import InputBotExseption
from goit_assistant_bot.commands import get_prompt_input, parse_input, commands_handler
from goit_assistant_bot.commands.commands import CMD_ADD_PHONE


class TestCommandsHandlerGetPromptInput(unittest.TestCase):
    """Tests get_prompt_input"""

    def setUp(self):
        pass

    @patch(
        "goit_assistant_bot.commands.handler.WordCompleter",
        return_value="wordCompleter",
    )
    @patch("goit_assistant_bot.commands.handler.prompt", return_value="help")
    def test_get_prompt_input_with_completer(self, mock_prompt, *_):
        """prompt should be called with completer"""
        output = get_prompt_input("Enter your command: ")
        mock_prompt.assert_called_once_with(
            "Enter your command: ", completer="wordCompleter"
        )
        # check return value
        self.assertEqual(output, "help")

    @patch(
        "goit_assistant_bot.commands.handler.WordCompleter",
        return_value="wordCompleter",
    )
    @patch("goit_assistant_bot.commands.handler.prompt", return_value="add-phone Max")
    def test_get_prompt_input(self, mock_prompt, *_):
        """prompt should be called with no completer"""
        output = get_prompt_input("Enter a command: ", False)
        mock_prompt.assert_called_once_with("Enter a command: ")
        # check return value
        self.assertEqual(output, "add-phone Max")

    @patch(
        "goit_assistant_bot.commands.handler.WordCompleter",
        return_value="wordCompleter",
    )
    @patch("goit_assistant_bot.commands.handler.prompt", return_value="help")
    def test_get_prompt_input_with_default_message(self, mock_prompt, *_):
        """prompt should be called with completer"""
        output = get_prompt_input()
        mock_prompt.assert_called_once_with(">>> ", completer="wordCompleter")
        # check return value
        self.assertEqual(output, "help")


class TestCommandsHandlerParseInput(unittest.TestCase):
    """Tests parse_input"""

    def setUp(self):
        pass

    def test_parse_input_with_command_no_args(self):
        """should return command, func and empty args"""
        cmd, cmd_func, args = parse_input(CMD_ADD_PHONE)
        self.assertEqual(cmd, CMD_ADD_PHONE)
        self.assertEqual(len(args), 0)
        self.assertTrue(callable(cmd_func))

    def test_parse_input_with_command_and_args(self):
        """should return command, func and not empty args"""
        cmd, cmd_func, args = parse_input(f"{CMD_ADD_PHONE} Maxima")
        self.assertEqual(cmd, CMD_ADD_PHONE)
        self.assertEqual(len(args), 1)
        self.assertEqual(args[0], "Maxima")
        self.assertTrue(callable(cmd_func))

    def test_parse_input_with_no_exists_command(self):
        """should return None for command, function and empty args"""
        cmd, cmd_func, args = parse_input("dummy-command")
        self.assertIsNone(cmd)
        self.assertIsNone(cmd_func)
        self.assertEqual(len(args), 0)

    def test_parse_input_with_exception(self):
        """should raise InputBotExseption for empty user_input"""
        with self.assertRaises(InputBotExseption):
            parse_input("")

        with self.assertRaises(InputBotExseption):
            parse_input(None)

        with self.assertRaises(InputBotExseption):
            parse_input("    ")


class TestCommandsHandlercommands_handler(unittest.TestCase):
    """Tests commands_handler"""

    def setUp(self):
        pass

    def test_commands_handler(self):
        """should call a command function."""
        book = AddressBook()
        mock_command_func = Mock()
        user_data = mock_command_func, ["Maxima"]
        commands_handler(book, user_data)
        mock_command_func.assert_called_once_with(["Maxima"], book)

    def test_commands_handler_no_insstance(self):
        """should not call a command function if there ia no instance of AddressBook."""
        mock_command_func = Mock()
        user_data = mock_command_func, ["Maxima"]
        commands_handler(None, user_data)
        mock_command_func.assert_not_called()

    def test_commands_handler_no_function(self):
        """should not call a command function if one is not callable."""
        mock_command_func = Mock()
        user_data = None, ["Maxima"]
        commands_handler(AddressBook(), user_data)
        mock_command_func.assert_not_called()


if __name__ == "__main__":
    unittest.main()
