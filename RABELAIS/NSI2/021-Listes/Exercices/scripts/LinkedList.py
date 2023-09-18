class Cell:
    """
    A simple cell class
    """

    def __init__(self, value, successor):
        self.value = value
        self.succ = successor


class LinkedList:

    def __init__(self):
        """
        Creates an empty linked_list
        """
        self.head = None

    def __getitem__(self, n):
        """
        Allows to write L[2] and such
        """
        current = self.head

        while current and n > 0:
            n -= 1
            current = current.succ
        if n > 0 or current is None:
            raise IndexError('Index out of range.')
        return current.value

    def __len__(self) -> int:
        """
        length of the linked list
        """
        result = 0
        current = self.head
        while current:
            result += 1
            current = current.succ
        return result

    def insert(self, value, n=0):
        """
        Inserts value at position n
        """
        if n == 0:
            self.head = Cell(value, self.head)
        else:
            replace = self[n - 1]
            if not replace:
                raise IndexError('Index out of range.')
            replace.succ = Cell(value, replace.succ)

    def __delitem__(self, n):
        """
        Removes n-th element
        """
        if not self.head:
            raise IndexError('IE')
        elif n == 0:
            self.head = self.head.succ
        else:
            n -= 1
        current = self.head
        while current and n > 0:
            n -= 1
            current = current.succ
        if n > 0:
            raise IndexError('IE')
        elif not current:
            raise IndexError('IE')
        if not current.succ:
            raise IndexError('IE')
        else:
            current.succ = current.succ.succ

    def extend(self, other):
        """
        Adds all the elements of the other list after current list's last one
        """
        if not self.head:
            self.head = other.head
        else:
            current = self.head
            while current.succ:
                current = current.succ
            current.succ = other.head

    def find(self, value) -> int:
        """
        Returns the index of value's first occurrence if value's present, otherwise -1
        """
        if not self.head:
            return -1

        current = self.head
        n = 0
        while current:
            if current.value == value:
                return n
            n += 1
            current = current.succ
        return -1

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

    def __eq__(self, other):
        current1, current2 = self.head, other.head
        while current1:
            if not current2 or current2.value != current1.value:
                return False
            current1 = current1.succ
            current2 = current2.succ
        if current2:
            return False
        return True
