import unittest
from insertion_sort import InsertionSort

class InsertionSortTest(unittest.TestCase):
  def test_sort(self):
    self.assertEqual([1, 2, 3, 4, 5], InsertionSort.sort([5, 4, 3, 2, 1]))
    

if __name__ == '__main__':
  unittest.main()