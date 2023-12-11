import string
import random
from datetime import datetime


def generate_uuid():
    """
    Generates and returns random 15 characters + timestamp

    Parameters: None

    Returns: str
    """

    choices = random.choices(string.ascii_letters + string.digits, k=15)
    return "".join(choices) + str(datetime.now())


__all__ = [
    "generate_uuid",
]
