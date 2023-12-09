import re
from colorama import Fore, Style
from ..constants import TEXT
from ..exceptions import ValidationValueExseption
from .field import Field

class NoteContent(Field):
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if len(new_value) > 10 and len(new_value) <= 500:
            self._value = new_value
        else:
            raise ValidationValueExseption(TEXT["NOTE_VALIDATION"])

    def __str__(self):
        return f'{self._value}'

    def __repr__(self):
        return f'Note: {self._value}'


class Tag(Field):
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if re.search(r"\w{1,15}", new_value):
            self._value = new_value
        else:
            raise ValidationValueExseption(TEXT["TAG_VALIDATION"])

    def __str__(self):
        return f'{self._value}'

    def __repr__(self):
        return f'Tag: {self._value}'

class Note:
    def __init__(self, content):
        self.content = NoteContent(content)
        self.tags = []

    def get_string_content(self, no_data_message = ""):
        return self.content.value if self.content else no_data_message

    def get_string_tags(self, no_data_message = "NO TAGS"):
        return " ".join("#" + str(tag) for tag in self.tags) if len(self.tags) > 0 else no_data_message

    def is_tag_exists(self, tag):
        for i in self.tags:
            if str(i).lower() == tag.lower():
                return True
        return False

    def remove_tag(self, tag):
        if self.is_tag_exists(tag):
            self.tags = list(filter(lambda t: t.value.lower() != tag.lower(), self.tags))
            print(TEXT["DELETED"])
            return True

        print(TEXT["NOT_FOUND"])
        return False

    def add_tag(self, tag):
        if self.is_tag_exists(tag):
            print(TEXT["EXISTS"])
            return False

        self.tags.append(Tag(tag))
        print(TEXT["ADDED"])
        return True

    def __str__(self):
        return self.get_string_tags() + "\n" + self.get_string_content()

__all__ = ["Note"]
