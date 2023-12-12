import unittest
from goit_assistant_bot.address_book.utils.uuid import generate_uuid


class TestUUID(unittest.TestCase):
    def test_run(self):
        uuid = generate_uuid()
        self.assertIn(":", uuid)
        self.assertGreaterEqual(34, len(uuid))


if __name__ == "__main__":
    unittest.main()
