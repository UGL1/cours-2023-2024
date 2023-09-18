from os import getpid

pid = str(getpid())
print(f'----------------------------------------start process {pid}')
for i in range(1000):
    print(f'process {pid}\t\t value {i}')
print(f'________________________________________end process {pid}')
