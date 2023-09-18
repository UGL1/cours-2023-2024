class Stack:
    def __init__(self):
        """ Creates an empty stack"""
        self.content = []

    def is_empty(self) -> bool:
        """ Indicates whether the stack's empty or not """
        return self.content == []

    def push(self, value):
        """ Pushes the value on the top of the stack """
        self.content.append(value)

    def pop(self):
        """ Retrieves the value from the top of the stack"""
        if self.is_empty():
            raise IndexError('Stack Empty')
        return self.content.pop()


