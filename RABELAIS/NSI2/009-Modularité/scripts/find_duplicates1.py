from duplicates1 import *
from random import randint


def has_duplicate(content: list) -> bool:
    s = create()
    for x in content:
        if contains(s, x):
            return True
        else:
            add(s, x)
    return False


test_list = [randint(1, 2 ** 16) for _ in range(302)]

print(has_duplicate(test_list))
