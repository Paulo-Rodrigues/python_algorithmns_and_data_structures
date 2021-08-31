import unittest
from selection_sort import SelectionSort

class SelectionSortTest(unittest.TestCase):
    def test_selection_sort(self):
      SelectionSort.sort(self, [5,7,6,3,9,1,2])
      self.assertEqual([1,2,3,5,6,7,9], [1,2,3,5,6,7,9])

if __name__ == "__main__":
    unittest.main()