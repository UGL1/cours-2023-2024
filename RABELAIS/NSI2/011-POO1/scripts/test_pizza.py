from pizza import *

my_pizza = Pizza()


assert not my_pizza.select_dough(Pizza.DOUGH_THIN), "Il doit être impossible de choisir la pâte d'abord"
assert not my_pizza.select_base(Pizza.BASE_TOMATO), "Il doit être impossible de choisir la sauce d'abord"
assert not my_pizza.add_ingredient("piments"), "Il doit être impossible d'ajouter des ingrédients d'abord"
assert not my_pizza.remove_ingredient("mercure"), "On ne peut pas retirer un ingrédient inexistant"
assert not my_pizza.select_size("XXXL"), "Il faut vérifier que les tailles sont valides"

assert my_pizza.select_size(Pizza.SIZE_XL), "PB : selection de la taille"

assert not my_pizza.select_base(Pizza.BASE_TOMATO), "Il doit être impossible de choisir la sauce d'abord"
assert not my_pizza.add_ingredient("piments"), "Il doit être impossible d'ajouter des ingrédients d'abord"
assert not my_pizza.remove_ingredient("mercure"), "On ne peut pas retirer un ingrédient inexistant"
assert not my_pizza.select_dough(Pizza.DOUGH_MOZZA_CRUST), "PB : respect des pâtes suivant les tailles"
assert not my_pizza.select_dough("Terre cuite"), "Vérifier que les pâtes sont valides"

assert my_pizza.select_dough(Pizza.DOUGH_THIN), "PB : selection de la pâte"

assert not my_pizza.add_ingredient("piments"), "Il doit être impossible d'ajouter des ingrédients d'abord"
assert not my_pizza.remove_ingredient("mercure"), "On ne peut pas retirer un ingrédient inexistant"
assert not my_pizza.select_base("dentifrice"), "Il doit être impossible de choisir la sauce d'abord"

assert my_pizza.select_base(Pizza.BASE_TOMATO), "PB : sélection de la sauce"
assert not my_pizza.remove_ingredient("mercure"), "On ne peut pas retirer un ingrédient inexistant"
assert my_pizza.add_ingredient(Pizza.ING_BACON), "PB : Ajout d'ingrédients"
assert my_pizza.add_ingredient(Pizza.ING_CHILIS), "PB : Ajout d'ingrédients"
assert my_pizza.add_ingredient(Pizza.ING_MOZZARELLA), "PB : Ajout d'ingrédients"
assert my_pizza.add_ingredient(Pizza.ING_BELL_PEPPERS), "PB : Ajout d'ingrédients"
assert my_pizza.add_ingredient(Pizza.ING_BELL_PEPPERS), "PB : Ajout d'ingrédients"
assert my_pizza.add_ingredient(Pizza.ING_BELL_PEPPERS), "PB : Ajout d'ingrédients"
assert not my_pizza.add_ingredient(Pizza.ING_BELL_PEPPERS), "PB : Ajout d'ingrédients dépasse 6 ingrédients"
assert my_pizza.remove_ingredient(Pizza.ING_BELL_PEPPERS), "PB : Retrait d'ingrédients"
assert not my_pizza.remove_ingredient("mercure"), "On ne peut pas retirer un ingrédient inexistant"

print(my_pizza)