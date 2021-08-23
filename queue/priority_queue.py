'''
 Priority Queue ordered list implementation
'''

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def __str__(self):
        return str(self.queue)
        
    def __len__(self):
        return len(self.queue)

    def enqueue(self, item, priority):
        self.queue.append((priority, self.index, item))
        self.index += 1
        self.queue.sort()

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)[2]

    def is_empty(self):
        return len(self.queue) == 0