class RectMap:
    whole_world_is_set = False
    top = None
    left = None
    width = None
    height = None
    center_x = None
    center_y = None
    min_dimension = None
    right = None
    bottom = None

    @classmethod
    def set_whole_world(cls, width=1, height=1, min_dimension=1):
        cls.top = 0
        cls.left = 0
        cls.width = width
        cls.height = height
        cls.min_dimension = min_dimension
        cls.center_x = int(round(width // 2))
        cls.center_y = int(round(height // 2))
        cls.right = cls.left + cls.width
        cls.bottom = cls.top + cls.height
        cls.whole_world_is_set = True
        cls.is_landscape = cls.width >= cls.height

    def __init__(self, left=0, top=0, width=1, height=1):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.constraint = height / width
        self.right = self.left + self.width
        self.bottom = self.top + self.height
        self.center_x = self.left + self.width / 2
        self.center_y = self.top + self.height / 2

    def translate(self, x=.0, y=.0):
        self.left += x
        self.top += y
        self.right += x
        self.bottom += y
        self.center_x += x
        self.center_y += y

    def translate_constrained(self, x=.0, y=.0):
        if 0 <= self.left + x <= RectMap.width \
                and 0 <= self.right + x <= RectMap.width \
                and 0 <= self.top + y <= RectMap.height \
                and 0 <= self.bottom + y <= RectMap.height:
            self.left += x
            self.top += y
            self.right += x
            self.bottom += y
            self.center_x += x
            self.center_y += y

    def set_left(self, left=0):
        self.translate(left - self.left, 0)

    def set_right(self, right=0):
        self.translate(right - self.right, 0)

    def set_top(self, top=0):
        self.translate(0, top - self.top)

    def set_bottom(self, bottom=0):
        self.translate(0, bottom - self.bottom)

    def set_center(self, x=0, y=0):
        self.translate(x - self.center_x, y - self.center_y)

    def set_width(self, width=1):
        self.width = width
        self.height = width * self.constraint
        self.left = self.center_x - self.width / 2
        self.top = self.center_y - self.height / 2
        self.right = self.left + self.width
        self.bottom = self.top + self.height

    def set_height(self, height=1):
        self.height = height
        self.width = height / self.constraint
        self.left = self.center_x - self.width / 2
        self.top = self.center_y - self.height / 2
        self.right = self.left + self.width
        self.bottom = self.top + self.height

    def dilate(self, factor=1):
        self.width *= factor
        self.height *= factor
        self.left = self.center_x - self.width / 2
        self.top = self.center_y - self.height / 2
        self.right = self.left + self.width
        self.bottom = self.top + self.height

    def zoom_out(self, factor):
        self.dilate(min(factor, RectMap.width / self.width, RectMap.height / self.height))
        if self.left < 0:
            self.set_left(0)
        if self.right > RectMap.width - 1:
            self.set_right(RectMap.width - 1)
        if self.top < 0:
            self.set_top(0)
        if self.bottom > RectMap.height - 1:
            self.set_bottom(RectMap.height - 1)
        if self.left < 0:
            self.translate(-self.left, 0)
            if self.width > RectMap.width - 1:
                self.width = RectMap.width - 1
        if self.top < 0:
            self.translate(0, -self.top)
            if self.bottom > RectMap.height - 1:
                self.bottom = RectMap.height - 1
        return self

    def zoom_factor(self):
        return self.width / RectMap.width

    def zoom_in(self, x, y, factor):
        if self.width * factor >= RectMap.min_dimension and self.height * factor >= RectMap.min_dimension:
            self.left = factor * self.left + (1 - factor) * x
            self.top = factor * self.top + (1 - factor) * y
            self.width = self.width * factor
            self.height = self.height * factor
            self.center_x = self.left + self.width / 2
            self.center_y = self.top + self.height / 2
            self.right = self.left + self.width
            self.bottom = self.top + self.height
        return self

    def __str__(self):
        return f"left={self.left}, top={self.top}, width={self.width},height={self.height},ff={self.constraint}"
