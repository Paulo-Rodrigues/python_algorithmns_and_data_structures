import unittest
from bubble_sort import BubbleSort

class BubbleSortTest(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(BubbleSort.sort(self, [5, 2, 3, 1, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(BubbleSort.sort(self, [5, 2, 3, 1, 4, 6, 7]), [1, 2, 3, 4, 5, 6, 7])

if __name__ == "__main__":
    unittest.main()