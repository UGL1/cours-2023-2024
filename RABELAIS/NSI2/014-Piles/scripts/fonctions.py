def fact(n : int) -> int:
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(fact(13))