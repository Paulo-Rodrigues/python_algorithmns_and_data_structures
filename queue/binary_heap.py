import heapq
import unittest

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class PriorityQueueTest(unittest.TestCase):
    def test_init(self):
        pq = PriorityQueue()
        self.assertIsNotNone(pq)

    def test_push(self):
        pq = PriorityQueue()
        pq.push('A', 1)
        self.assertEqual(pq._queue, [(-1, 0, 'A')])
        pq.push('B', 2)
        self.assertEqual(pq._queue, [(-2, 1, 'B'), (-1, 0, 'A')])


if __name__ == '__main__':
    unittest.main()