class MyList:

    def __init__(self):
        self.content = [None] * 10
        self.changes = 0

    def __setitem__(self, key, value):  # permet de changer un élément
        self.content[key] = value
        self.changes += 1

    def __delitem__(self, key):
        self.content[key] = None

    def __getitem__(self, key):  # accès à l'élément
        return self.content[key]

    def __len__(self):  # pour utiliser len
        return len([x for x in self.content if x is not None])

    def __iter__(self):  # pour itérer sur les éléments
        return iter([x for x in self.content if x is not None])


    def __in__(self, item): # pour utiliser in
        return item in self.content
