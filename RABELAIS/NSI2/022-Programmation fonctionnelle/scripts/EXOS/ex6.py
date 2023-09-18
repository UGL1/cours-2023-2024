from time import perf_counter


def get_execution_time(f, x):
    start = perf_counter()
    f(x)
    return perf_counter() - start


def sum_first_int(n):
    return sum(i for i in range(n + 1))


duration = get_execution_time(sum_first_int, 10**8)
print(f"Duration : {duration} milliseconds.")
