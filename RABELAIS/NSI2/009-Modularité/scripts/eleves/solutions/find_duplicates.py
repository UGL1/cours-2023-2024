from solutions.duplicates4 import *  # doit marcher avec tes modules duplicate2 duplicate3 et duplicate4
from random import randint



def has_duplicate(content: list) -> bool:
    """
    Le code de cette fonction NE DOIT PAS changer
    """
    s = create()
    for x in content:
        if contains(s, x):
            return True
        else:
            add(s, x)
    return False


test_list = [randint(1, 2 ** 16) for _ in range(302)]

print(has_duplicate(test_list))
