import sys, os
from time import perf_counter,sleep


def compile(f: str) -> float:
    now = perf_counter()
    os.system("lualatex -shell-escape -synctex=1 -interaction=batchmode " + f)
    return perf_counter() - now


file = "cours.tex"
now = perf_counter()
print(f"Compiling {file}")
ctime = compile(file)
print("-"*80)
print(f"{file} compiled in {ctime} seconds.")
print("-"*80)