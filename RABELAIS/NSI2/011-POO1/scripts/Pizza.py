class Pizza:
    SIZE_M = "M"
    SIZE_L = "L"
    SIZE_XL = "XL"
    SIZE_PRICE = {
        SIZE_M: 7.99,
        SIZE_L: 7.99,
        SIZE_XL: 16.5
    }
    SIZE_LIST = SIZE_PRICE.keys()

    DOUGH_MOZZA_CRUST = "mozza crust"
    DOUGH_PAN = "pan"
    DOUGH_THIN = "thin"
    DOUGH_REGULAR = "regular"
    DOUGH_PRICE = {
        DOUGH_MOZZA_CRUST: 2.90,
        DOUGH_PAN: 1.50,
        DOUGH_REGULAR: 0,
        DOUGH_THIN: 0
    }
    DOUGH_LIST = DOUGH_PRICE.keys()

    BASE_CREAM = "base crème"
    BASE_BBQ = "base bbq"
    BASE_TOMATO = "base tomate"
    BASE_PRICE = {
        BASE_CREAM: 0,
        BASE_BBQ: 0,
        BASE_TOMATO: 0,
    }
    BASE_LIST = BASE_PRICE.keys()

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
    INGREDIENT_LIST = INGREDIENT_PRICE.keys()

    orders = []
    total_income = 0

    @classmethod
    def order(cls, p):
        cls.orders.append(p)
        cls.total_income += p.get_price()

    def __init__(self):
        self.size = None
        self.dough = None
        self.base = None
        self.ingredients = []

    def select_size(self, size) -> bool:

        if not self.size and size in Pizza.SIZE_LIST:
            self.size = size
            return True
        else:
            return False

    def select_dough(self, dough) -> bool:
        if self.size == Pizza.SIZE_M and dough in Pizza.DOUGH_LIST:
            self.dough = dough
            return True
        elif self.size == Pizza.SIZE_L and dough in (Pizza.DOUGH_THIN, Pizza.DOUGH_PAN):
            self.dough = dough
            return True
        elif self.size == Pizza.SIZE_XL and dough == Pizza.DOUGH_THIN:
            self.dough = dough
            return True
        else:
            return False

    def select_base(self, base) -> bool:
        if self.size and self.dough and base in Pizza.BASE_LIST:
            self.base = base
            return True
        else:
            return False

    def add_ingredient(self, ingredient) -> bool:
        if self.size and self.dough and self.base and len(self.ingredients) < 6 and ingredient in Pizza.INGREDIENT_LIST:
            self.ingredients.append(ingredient)
            return True
        else:
            return False

    def remove_ingredient(self, ingredient) -> bool:
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            return True
        else:
            return False

    def get_price(self) -> float:
        total = Pizza.SIZE_PRICE[self.size]
        total += Pizza.DOUGH_PRICE[self.dough]
        total += Pizza.BASE_PRICE[self.base]
        for i in self.ingredients:
            total += Pizza.INGREDIENT_PRICE[i]
        return total

    def __str__(self) -> str:
        result = "Pizza\n"
        result += "\tTaille : " + str(self.size) + "\n"
        result += "\tPâte   : " + str(self.dough) + "\n"
        result += "\tBase   : " + str(self.base) + "\n"
        result += "\tIngrédients : \n"
        for i in self.ingredients:
            result += "\t\t" + str(i) + "\n"
        return result
