import unittest
from queue import Queue

class QueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
    
    def test_isEmpty(self):
        self.assertTrue(self.queue.isEmpty())
    
    def test_enqueue(self):
        self.queue.enqueue(1)

        self.assertFalse(self.queue.isEmpty())

    def test_dequeue(self):
        self.queue.enqueue(1)
        
        self.assertEqual(self.queue.dequeue(), 1)

    def test_size(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.assertEqual(self.queue.size(), 2)

    def test_peek(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.assertEqual(self.queue.peek(), 1)

    def test_str(self):
        self.queue.enqueue(1)
        
        self.assertEqual(str(self.queue), "[1]")

    def test_repr(self):
        self.queue.enqueue(1)

        self.assertEqual(repr(self.queue), "[1]")

    def tearDown(self):
        self.queue = None

if __name__ == "__main__":
    unittest.main()