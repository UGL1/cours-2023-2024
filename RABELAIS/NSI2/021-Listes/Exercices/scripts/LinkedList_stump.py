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
                raise IndexError('LinkedList : index out of range')
            replace.succ = Cell(value, replace.succ)

    def __delitem__(self, n):
        """
        Removes n-th element
        """
        if not self.head:
            raise IndexError('LinkedList : cannot delete from empty list')
        elif n == 0:
            self.head = self.head.succ
        else:
            n -= 1
        current = self.head
        while current and n > 0:
            n -= 1
            current = current.succ
        if n > 0:
            raise IndexError('LinkedList : index out of range')
        elif not current:
            raise IndexError('LinkedList : index out of range')
        if not current.succ:
            raise IndexError('LinkedList : index out of range')
        else:
            current.succ = current.succ.succ

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

    def find(self, value) -> int:
        """
        Returns the index of value's first occurrence if value's present, otherwise -1
        """
        pass

    def extend(self, other):
        """
        Adds all the elements of the other list after current list's last one
        """
        pass

    def __eq__(self, other):
        pass
