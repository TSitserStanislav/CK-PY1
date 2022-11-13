import random
import string


def get_random_password() -> str:
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 8
    return "".join(random.sample(chars, size))

print(get_random_password())
