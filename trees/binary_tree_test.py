import unittest
from binary_tree import BinarySearchTree

class BinarySearchTreeTest(unittest.TestCase):
    def setup(self):
        self.tree = BinarySearchTree(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(13)
        self.tree.insert(17)
        self.tree.insert(1)

    def test_insert(self):
        self.setup()
        self.assertEqual(self.tree.contains(5), True)

    def test_contains(self):
        self.setup()
        self.assertEqual(self.tree.contains(5), True)

    def test_contains_false(self):
        self.setup()
        self.assertEqual(self.tree.contains(6), False)

if __name__ == '__main__':
    unittest.main()