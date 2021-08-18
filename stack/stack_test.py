import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_isEmpty(self):
        self.assertTrue(self.stack.isEmpty())

    def test_push(self):
        self.stack.push(1)

        self.assertFalse(self.stack.isEmpty())

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.isEmpty())

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.peek(), 2)

    def test_size(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.size(), 2)

    def test_str(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(str(self.stack), "[1, 2]")

    def test_repr(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(repr(self.stack), "[1, 2]")

    def tearDown(self):
        self.stack = None

if __name__ == '__main__':
    unittest.main()