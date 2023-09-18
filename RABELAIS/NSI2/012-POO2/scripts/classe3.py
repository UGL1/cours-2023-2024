class Person:
    def __init__(self, a: int, n: str, s: str):
        self._age = a
        self._name = n
        self._surname = s

    def get_age(self) -> int:
        return self._age

    def set_age(self, a: int):
        self._age = a

    def get_name(self) -> str:
        return self._name

    def set_name(self, n: str):
        self._name = n

    def get_surname(self) -> str:
        return self._surname

    def set_surname(self, s: str):
        self._surname = s

    def __str__(self):
        return "Name : " + self._name + ", Surname : " + self._surname + ", Age : " + str(self._age)

    def __eq__(self, other):
        return self._age == other._age and self._name == other._name and self._surname == other._surname

    def __lt__(self, other):
        return self._age < other._age




