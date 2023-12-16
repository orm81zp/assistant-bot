import re
from ..constants import (
    TEXT,
    NOT_FOUND,
    EXISTS,
    DELETED,
    ADDED,
)
from ..utils import print_message
from ..exceptions import ValidationValueException
from .field import Field

not_found_message = print_message(NOT_FOUND)
exists_message = print_message(EXISTS)
deleted_message = print_message(DELETED)
added_message = print_message(ADDED)


class NoteContent(Field):
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value and len(new_value) > 10 and len(new_value) <= 500:
            self._value = new_value
        else:
            raise ValidationValueException(TEXT["NOTE_VALIDATION"])

    def __str__(self):
        return f"{self._value}"

    def __repr__(self):
        return f"Note: {self._value}"


class Tag(Field):
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value and re.search(r"^\w{1,15}$", new_value):
            self._value = new_value
        else:
            raise ValidationValueException(TEXT["TAG_VALIDATION"])

    def __str__(self):
        return f"{self._value}"

    def __repr__(self):
        return f"Tag: {self._value}"


class Note:
    def __init__(self, content, uuid):
        self.__content = NoteContent(content)
        self.uuid = uuid
        self.tags = []

    @property
    def content(self):
        return self.__content.value if self.__content else ""

    @content.setter
    def content(self, new_value):
        self.__content = NoteContent(new_value)

    def get_content(self, no_data_message=""):
        return self.content or no_data_message

    def get_tags(self, no_data_message="no tags"):
        return (
            " ".join(str(tag) for tag in self.tags)
            if len(self.tags) > 0
            else no_data_message
        )

    def tag_exists(self, tag):
        for itag in self.tags:
            if str(itag).lower() == tag.lower():
                return True
        return False

    def remove_tag(self, tag):
        if self.tag_exists(tag):
            self.tags = list(filter(lambda t: str(t).lower() != tag.lower(), self.tags))
            deleted_message("Tag")
            return True

        not_found_message("Tag")
        return False

    def add_tag(self, tag):
        if self.tag_exists(tag):
            exists_message("The same tag")
            return False

        print("ADDING A TAG: ", tag)
        self.tags.append(Tag(tag))
        added_message("Tag")
        return True

    def __str__(self):
        return self.get_tags() + "; " + str(self.uuid) + "; " + self.get_content()

    def __repr__(self):
        return (
            "Note: "
            + self.get_tags()
            + "; "
            + str(self.uuid)
            + "; "
            + self.get_content()
        )


__all__ = ["Note"]
