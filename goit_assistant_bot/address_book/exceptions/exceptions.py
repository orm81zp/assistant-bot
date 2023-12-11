class ValidationValueExseption(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


__all__ = ["ValidationValueExseption"]
