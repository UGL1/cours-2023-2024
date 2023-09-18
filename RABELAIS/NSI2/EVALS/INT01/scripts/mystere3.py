def mystery3(lst: list) -> bool:
    if len(lst) > 1:
        if lst[0] > lst[1]:
            return False
        else:
            return mystery3(lst[1:])

    else:
        return True
