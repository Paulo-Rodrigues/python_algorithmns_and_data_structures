class MyQuickSort:
  @staticmethod
  def sort(array, left, right):
    if left < right:
      p = MyQuickSort.partition(array, left, right)
      MyQuickSort.sort(array, left, p - 1)
      MyQuickSort.sort(array, p + 1, right)
    return array

  @staticmethod
  def partition(array, left, right):
    pivot = array[(left + right) // 2]
    while left <= right:
      while array[left] < pivot:
        left += 1
      while array[right] > pivot:
        right -= 1
      if left <= right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return left