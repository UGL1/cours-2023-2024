from Cell import *


class LinkedList:
    def __init__(self, values=None):
        if not values:
            self.head = None
        else:
            self.head = Cell(values[0])
            current = self.head
            for i in range(1, len(values)):
                current.succ = Cell(values[i])
                current = current.succ

    def get_cell(self, position):
        current = self.head
        while position:
            if not current:
                raise IndexError
            current = current.succ
            position -= 1
        return current

    def insert(self, value, position: int) -> None:
        new_cell = Cell(value)
        if not position:
            new_cell.succ = self.head
            self.head = new_cell
        else:
            cell_before = self.get_cell(position - 1)
            new_cell.succ = cell_before.succ
            cell_before.succ = new_cell

    def remove(self, position):
        if not position:
            if not self.head:
                raise IndexError
            else:
                self.head = self.head.succ
        else:
            cell_before = self.get_cell(position - 1)
            if not cell_before.succ:
                raise IndexError
            cell_before.succ = cell_before.succ.succ

    def get_element(self, position: int):
        current = self.head
        while position:
            if current:
                current = current.succ
                position -= 1
            else:
                raise IndexError
        return current.value

    def length(self) -> int:
        result = 0
        current = self.head
        while current:
            result += 1
            current = current.succ
        return result

    def extend(self, other):
        current = self.head
        if not current:
            self.head = other.head
        else:
            while current.succ:
                current = current.succ
            current.succ = other.head

    def is_equal(self, other):
        cur1, cur2 = self.head, other.head
        if not ((cur1 and cur2) or not cur1 and not cur2):
            return False
        while cur1 and cur2:
            if cur1.value != cur2.value:
                return False
            cur1 = cur1.succ
            cur2 = cur2.succ
        return not (cur1 or cur2)

    def __str__(self):
        """
        Trying to make things pretty
        """
        if not self.head:
            return '<empty>'
        else:
            current = self.head
            result = '< ' + str(current.value) + ', '
            while current.succ:
                current = current.succ
                result += str(current.value) + ', '
            return result[:-2] + ' >'
