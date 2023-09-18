from Pizza import *

my_pizza = Pizza()
my_pizza.select_size(Pizza.SIZE_M)
my_pizza.select_dough(Pizza.DOUGH_MOZZA_CRUST)
my_pizza.select_base(Pizza.BASE_TOMATO)
my_pizza.add_ingredient(Pizza.ING_BACON)
my_pizza.add_ingredient(Pizza.ING_CHILIS)
my_pizza.add_ingredient(Pizza.ING_MOZZARELLA)
my_pizza.add_ingredient(Pizza.ING_BELL_PEPPERS)
Pizza.order(my_pizza)
print(my_pizza)