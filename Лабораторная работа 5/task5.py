import random
import string

def get_random_password (size = 8) -> str:
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(random.sample(chars, size))

print(get_random_password())
