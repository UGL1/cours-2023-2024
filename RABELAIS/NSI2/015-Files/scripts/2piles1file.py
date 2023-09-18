from stack import *


class QueueWith2Stacks:
    def __init__(self):
        self.entrance = Stack()
        self.exit = Stack()

    def enqueue(self,value):
        self.entrance.push(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Empty queue.')
        if self.exit.is_empty():
            while not self.entrance.is_empty():
                self.exit.push(self.entrance.pop())
        return self.exit.pop()

    def is_empty(self):
        return self.exit.is_empty() and self.entrance.is_empty()


q = QueueWith2Stacks()

q.enqueue(2)
q.enqueue(4)
print(q.dequeue())
print(q.is_empty())
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())

print(q.is_empty())