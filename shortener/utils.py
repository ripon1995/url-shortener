import string

BASE62_ALPHABET = string.digits + string.ascii_letters  # 0-9, A-Z, a-z


def encode_base62(num):
    if num == 0:
        return BASE62_ALPHABET[0]
    base62 = ""
    while num:
        num, rem = divmod(num, 62)
        base62 = BASE62_ALPHABET[rem] + base62
    return base62
