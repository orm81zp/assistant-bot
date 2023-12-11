import string
import random
from time import time


def generate_uuid():
    """
    Generates and returns random 15 characters + timestamp

    Parameters: None

    Returns: str
    """

    choices = random.choices(string.ascii_letters + string.digits, k=15)
    return "".join(choices) + ":" + str(time())


__all__ = [
    "generate_uuid",
]
