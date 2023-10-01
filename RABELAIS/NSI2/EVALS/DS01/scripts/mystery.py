def mystery(lst: list) -> list:
    if len(lst) < 2:
        return lst
    else:
        return [lst[-1]] + mystery(lst[1:-1]) + [lst[0]]
