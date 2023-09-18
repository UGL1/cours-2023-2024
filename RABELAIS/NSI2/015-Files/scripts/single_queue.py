from queue import Queue
from random import randint

now = 0


class CheckOut:
    nb_checkouts = 0
    total_waiting_time = 0
    checkouts = []

    def __init__(self, queue: Queue):
        self.queue = queue
        self.waiting_time = 0
        CheckOut.nb_checkouts += 1
        CheckOut.checkouts.append(self)

    def serve(self):
        assert self.waiting_time == 0
        CheckOut.total_waiting_time += now - self.queue.dequeue()
        self.waiting_time = randint(1, CheckOut.nb_checkouts)

    def update(self):
        self.waiting_time = max(0, self.waiting_time - 1)

    def is_free(self):
        return self.waiting_time == 0


queue = Queue()
for i in range(20):
    CheckOut(queue)
    queue.enqueue(now)

n = 100_000
for _ in range(n):
    now += 1
    queue.enqueue(now)
    for c in CheckOut.checkouts:
        c.update()
        if c.is_free() and not c.queue.is_empty():
            c.serve()
print(CheckOut.total_waiting_time/(n-len(queue)))
 