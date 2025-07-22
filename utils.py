import string
import random
import hashlib
import base64

BASE62 = string.ascii_letters + string.digits

def base62_encode(num):
    if num == 0:
        return BASE62[0]
    result = []
    while num:
        num, rem = divmod(num, 62)
        result.append(BASE62[rem])
    return ''.join(reversed(result))

def generate_short_code():
    # Gera um número pseudoaleatório e codifica em base62
    rand_num = random.getrandbits(48)
    return base62_encode(rand_num)
