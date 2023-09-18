def mystery2(lst: list) -> int:
    return 0 if lst == [] else 1 + mystery2(lst[1:])