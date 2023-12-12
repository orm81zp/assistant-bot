class Field:
    def __init__(self, new_value=""):
        self._value = new_value

    def __eq__(self, other):
        if isinstance(other, Field):
            return self._value == other._value

        return self._value == other

    def __str__(self):
        return str(self._value)


__all__ = ["Field"]
