class Queue:

    def __init__(self):
        self.content = []

    def enqueue(self, value):
        self.content = [value] + self.content

    def dequeue(self):
        if not self.content:
            raise IndexError('Empty Queue')
        return self.content.pop()

    def is_empty(self):
        return not self.content

    def __len__(self):  # Juste là pour l'exo sur les caisses
        return len(self.content)

    def __str__(self):
        return str(self.content)