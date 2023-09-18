class Rectangle:
    rectangle_list = []

    @classmethod
    def numbers_of_rectangles(cls):
        return len(cls.rectangle_list)

    def __init__(self, w: float, h: float):
        self.width = w
        self.height = h
        Rectangle.rectangle_list.append(self)

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height

    def rescale_by_factor(self, f: float):
        self.width *= f
        self.height *= f


