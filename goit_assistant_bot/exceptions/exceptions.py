class InputBotExseption(Exception):
    pass

class ValidationValueExseption(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UnexpectedException(Exception):
    pass

__all__ = [
    "InputBotExseption",
    "ValidationValueExseption",
    "UnexpectedException"
]
