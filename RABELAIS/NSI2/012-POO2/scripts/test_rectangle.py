from rectangle import *

r1 = Rectangle(10, 20, 100, 200)
print((3, 4) in r1)
print((12, 100) in r1)
r2 = Rectangle(30, 40, 50, 300)
print(r1 + r2)
print(r1 * r2)
