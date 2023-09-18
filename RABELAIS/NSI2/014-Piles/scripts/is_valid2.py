def is_valid(expression: str) -> bool:
    filtered = "".join(x for x in expression if x in "[({})]")
    print(filtered)
    found = True
    while found:
        i = 0
        found = False
        while not found and i < len(filtered) - 1:
            if filtered[i:i + 2] in ["()", "[]", "{}"]:
                found = True
                filtered = filtered[:i] + filtered[i + 2:]
            else:
                i += 1
    return not filtered

print(is_valid("{[(3*a+2*b)-4*(a+8)]/(2*x+y)+1}*(3*a+4)"))
