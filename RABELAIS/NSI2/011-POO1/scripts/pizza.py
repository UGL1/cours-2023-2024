class Pizza:
    # Ici on met toutes les constantes de la classe
    # par exemple SIZE_M sera accessible avec Pizza.SIZE_M

    # -------------------------------------------

    SIZE_M = "M"
    SIZE_L = "L"
    SIZE_XL = "XL"
    SIZE_PRICE = {  # dico des prix des tailles
        SIZE_M: 7.99,
        SIZE_L: 7.99,
        SIZE_XL: 16.5
    }
    SIZE_LIST = list(SIZE_PRICE.keys())  # liste des tailles

    # -------------------------------------------

    DOUGH_MOZZA_CRUST = "mozza crust"
    DOUGH_PAN = "pan"
    DOUGH_THIN = "fine"
    DOUGH_REGULAR = "classique"
    DOUGH_PRICE = {  # dico des prix des pâtes
        DOUGH_MOZZA_CRUST: 2.90,
        DOUGH_PAN: 1.50,
        DOUGH_REGULAR: 0,
        DOUGH_THIN: 0
    }
    DOUGH_LIST = list(DOUGH_PRICE.keys())  # liste des pâtes

    # -------------------------------------------

    BASE_CREAM = "base crème"
    BASE_BBQ = "base bbq"
    BASE_TOMATO = "base tomate"
    BASE_PRICE = {  # dico des prix des sauces de base (ils peuvent changer, merci l'inflation)
        BASE_CREAM: 0,
        BASE_BBQ: 0,
        BASE_TOMATO: 0,
    }
    BASE_LIST = list(BASE_PRICE.keys())  # liste des sauces de base

    # -------------------------------------------

    ING_ANANAS = "ananas"
    ING_BACON = "bacon"
    ING_BEEF_BALLS = "boulettes boeuf"
    ING_MUSHROOMS = "champignons"
    ING_MOZZARELLA = "mozzarella"
    ING_ONIONS = "oignons"
    ING_BELL_PEPPERS = "poivrons"
    ING_CHILIS = "piments"
    INGREDIENT_PRICE = {
        ING_ANANAS: 1.30,
        ING_BACON: 2.00,
        ING_BEEF_BALLS: 1.80,
        ING_MUSHROOMS: 1.30,
        ING_MOZZARELLA: 2,
        ING_ONIONS: 1,
        ING_BELL_PEPPERS: 1.5,
        ING_CHILIS: 1
    }
    INGREDIENT_LIST = list(INGREDIENT_PRICE.keys())

    # ----------------------------------------

    def __init__(self):
        self.size = None
        self.dough = None
        self.base = None
        self.ingredients = []

    def select_size(self, size) -> bool:
        """
        Je fais renvoyer True si tout s'est bien passé, et False s'il y a un problème.
        Pareil pour les autres méthodes.
        """
        if self.size:
            print("Taille déjà choisie.")
            return False
        elif size not in Pizza.SIZE_LIST:
            print("Taille non valide.")
            return False
        else:
            self.size = size
            print(f"Taille choisie : {size}.")
            return True

    def select_dough(self, dough) -> bool:
        if not self.size:
            print("Il faut d'abord choisir la taille.")
            return False
        elif self.dough:
            print("Pâte déjà choisie.")
            return False
        elif dough not in Pizza.DOUGH_LIST:
            print("Pâte inconnue.")
            return False
        elif self.size == Pizza.SIZE_M and dough in Pizza.DOUGH_LIST:
            self.dough = dough
        elif self.size == Pizza.SIZE_L and dough in (Pizza.DOUGH_THIN, Pizza.DOUGH_PAN):
            self.dough = dough
        elif self.size == Pizza.SIZE_XL and dough == Pizza.DOUGH_THIN:
            self.dough = dough
        else:
            print(f"Pâte invalide pour cette taille ({self.size}).")
            return False
        print(f"Pâte choisie : {dough}.")
        return True

    def select_base(self, base) -> bool:
        if not self.size:
            print("Il faut d'abord choisir la taille.")
            return False
        elif not self.dough:
            print("Il faut d'abord choisir la pâte.")
            return False
        elif self.base:
            print("Base déjà choisie.")
        elif base not in Pizza.BASE_LIST:
            print("Sauce invalide.")
        else:
            self.base = base
            print(f"Base choisie : {base}.")
            return True

    def add_ingredient(self, ingredient) -> bool:
        if not all((self.size, self.base, self.dough)):
            print("Veuillez choisir la taille, la pâte et la sauce d'abord.")
            return False
        elif len(self.ingredients) >= 6:
            print("Vous avez déjà 6 ingrédients.")
            print(f"liste des ingrédients : {self.ingredients}.")
            return False
        elif ingredient not in Pizza.INGREDIENT_LIST:
            print("Ingrédient non valide.")
            return False
        else:
            self.ingredients.append(ingredient)
            print(f"Ingrédient {ingredient} ajouté.")
            print(f"liste des ingrédients : {self.ingredients}.")
            return True

    def remove_ingredient(self, ingredient) -> bool:
        if not all((self.size, self.base, self.dough)):
            print("Veuillez choisir la taille, la pâte et la sauce d'abord.")
            return False
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            print(f"Ingrédient {ingredient} retiré.")
            print(f"liste des ingrédients : {self.ingredients}.")
            return True
        else:
            print("Cet ingrédient n'est pas dans la liste.")

    def get_price(self) -> float:
        total = Pizza.SIZE_PRICE[self.size]
        total += Pizza.DOUGH_PRICE[self.dough]
        total += Pizza.BASE_PRICE[self.base]
        for i in self.ingredients:
            total += Pizza.INGREDIENT_PRICE[i]
        return total

    def __str__(self) -> str:
        """
        Ca, c'est cadeau !
        """
        result = "Pizza\n"
        result += "\tTaille : " + str(self.size) + "\n"
        result += "\tPâte   : " + str(self.dough) + "\n"
        result += "\tBase   : " + str(self.base) + "\n"
        result += "\tIngrédients : \n"
        for i in self.ingredients:
            result += "\t\t" + str(i) + "\n"
        return result
