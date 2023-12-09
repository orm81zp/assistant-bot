import string
import random
import datetime

def generate_uuid(extra = None):
    ct = datetime.datetime.now()
    variants = (extra if extra else "") + string.ascii_letters + "1234567890" + str(ct)
    choices = random.choices(variants, k=15)
    return "".join(choices)

__all__ = [
    "generate_uuid",
]
