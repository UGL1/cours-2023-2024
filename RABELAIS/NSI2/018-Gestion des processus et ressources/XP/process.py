class Process:
    def __init__(self, name, start, duration, priority=0,color=None):
        self.name = name
        self.start = start
        self.duration = duration
        self.priority = priority
        self.color = color
        if not color:
            self.color = 'blue'

