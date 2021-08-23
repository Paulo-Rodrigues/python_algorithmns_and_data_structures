import unittest
from priority_queue import PriorityQueue

class PriorityQueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = PriorityQueue()

    def test_enqueue(self):
        self.queue.enqueue('a', 1)
        self.queue.enqueue('b', 2)
        self.queue.enqueue('c', 3)
        self.assertEqual(self.queue.queue, [(1, 0, 'a'), (2, 1, 'b'), (3, 2, 'c')])
        
    def test_dequeue(self):
        self.queue.enqueue('a', 1)
        self.queue.enqueue('b', 2)
        self.queue.enqueue('c', 3)

        self.assertEqual(self.queue.dequeue(), 'a')

if __name__ == '__main__':
    unittest.main()