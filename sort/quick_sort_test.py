import unittest
from quick_sort import MyQuickSort

class MyQuickSortTestCase(unittest.TestCase):
  def test_sort(self):
    array = [3, 2, 1, 4, 5]
    MyQuickSort.sort(array, 0, len(array) - 1)
    self.assertEqual(array, [1, 2, 3, 4, 5])

if __name__ == '__main__':
  unittest.main()