import unittest
from deque import Deque

class DequeTest(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_isEmpty(self):
        self.assertTrue(self.deque.isEmpty())

    def test_addFront(self):
        self.deque.addFront(1)
        self.assertFalse(self.deque.isEmpty())

    def test_addRear(self):
        self.deque.addRear(1)
        self.assertFalse(self.deque.isEmpty())

    def test_removeFront(self):
        self.deque.addFront(1)
        self.deque.removeFront()
        self.assertTrue(self.deque.isEmpty())

    def test_removeRear(self):
        self.deque.addRear(1)
        self.deque.removeRear()
        self.assertTrue(self.deque.isEmpty())

    def test_size(self):
        self.deque.addFront(1)
        self.deque.addRear(2)
        self.assertEqual(self.deque.size(), 2)

    def test_str(self):
        self.deque.addFront(1)
        self.deque.addRear(2)
        self.assertEqual(str(self.deque), "[2, 1]")

    def tearDown(self):
        self.deque = None

if __name__ == "__main__":
    unittest.main()