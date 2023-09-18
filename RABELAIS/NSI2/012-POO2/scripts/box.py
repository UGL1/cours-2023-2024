class Box:

    def __init__(self, left: int, top: int, width: int, height: int):
        try:
            assert isinstance(left, int) and isinstance(top, int) and isinstance(width, int) and isinstance(height, int)
        except AssertionError:
            raise TypeError('Box : all parameters must be integers')
        try:
            assert left >= 0 and top >= 0 and width >= 0 and height >= 0
        except AssertionError:
            raise ValueError('Box : all parameters must be positive')
        self._left = left
        self._top = top
        self._width = width
        self._height = height
        self._right = left + width
        self._bottom = top + height

    def set_left(self, left: int):
        try:
            assert isinstance(left, int)
        except AssertionError:
            raise TypeError('set_left : parameter must be integer')
        try:
            assert left >= 0
        except AssertionError:
            raise ValueError('sef_left : parameter must be positive')
        self._left = left
        self._right = left + self._width

    def set_top(self, top: int):
        try:
            assert isinstance(top, int)
        except AssertionError:
            raise TypeError('set_top : parameter must be integer')
        try:
            assert top >= 0
        except AssertionError:
            raise ValueError('sef_top : parameter must be positive')
        self._top = top
        self._bottom = top + self._height

    def set_height(self, height: int):
        try:
            assert isinstance(height, int)
        except AssertionError:
            raise TypeError('set_height : parameter must be integer')
        try:
            assert height >= 0
        except AssertionError:
            raise ValueError('sef_left : parameter must be positive')
        self._height = height
        self._bottom = self._top + height

    def set_width(self, width: int):
        try:
            assert isinstance(width, int)
        except AssertionError:
            raise TypeError('set_width : parameter must be integer')
        try:
            assert width >= 0
        except AssertionError:
            raise ValueError('sef_width : parameter must be positive')
        self._width = width
        self._right = width + self._left

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def get_top(self):
        return self._top

    def get_bottom(self):
        return self._bottom

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def __add__(self, other):
        left = min(self._left, other.get_left())
        top = min(self._top, other.get_top())
        right = max(self._right, other.get_right())
        bottom = max(self._bottom, other.get_bottom())
        return Box(left, top, right - left, bottom - top)

    def __str__(self):
        return 'left : ' + str(self._left) + ', top : ' + str(self._top) + ', width : ' + str(
            self._width) + ', height : ' + str(self._height)

    def intersects(self, other):
        condition_1 = self._left <= other.get_left() <= self._right or other.get_left() <= self._left <= other.get_right()
        condition_2 = self._top <= other.get_top() <= self._bottom or other.get_top() <= self._top <= other.get_bottom()
        return condition_1 and condition_2

    def intersection(self, other):
        try:
            assert self.intersects(other)
        except AssertionError:
            raise ValueError('intersection : rectangles must intersect')
        left = max(self._left, other.get_left())
        top = max(self._top, other.get_top())
        right = min(self._right, other.get_right())
        bottom = min(self._bottom, other.get_bottom())
        return Box(left, top, right - left, bottom - top)

    def reunion(self, other):
        left = min(self._left, other.get_left())
        top = min(self._top, other.get_top())
        right = max(self._right, other.get_right())
        bottom = max(self._bottom, other.get_bottom())
        return Box(left, top, right - left, bottom - top)

    def __contains__(self, t):
        try:
            assert isinstance(t, tuple) or isinstance(t, list)
        except AssertionError:
            raise TypeError('__contains__ : parameter must be tuple or list')
        try:
            assert len(t) == 2
        except AssertionError:
            raise TypeError('__contains__ : length of parameter must be 2')

        return self._left <= t[0] <= self._right and self._top <= t[1] <= self._bottom

    def zoom(self, factor: float):
        try:
            assert isinstance(factor, float) or isinstance(factor, int)
        except AssertionError:
            raise TypeError('zoom : factor must be float or int')
        try:
            assert factor > 0
        except AssertionError:
            raise ValueError('zoom : factor must be strictly positive')


r1 = Box(10, 20, 100, 200)

r2 = Box(30, 40, 50, 300)
print(r1.reunion(r2))
