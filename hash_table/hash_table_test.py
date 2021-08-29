import unittest
from hash_table import HashTable

class HashTableTest(unittest.TestCase):
    def setUp(self):
        self.table = HashTable(10)
        self.table.insert(1, 'one')
        self.table.insert(2, 'two')

    def test_insert(self):
        self.assertEqual(self.table.search(1), 'one')
        self.assertEqual(self.table.search(2), 'two')
        self.assertEqual(self.table.search(3), None)

    def test_delete(self):
        self.table.delete(1)
        self.assertEqual(self.table.search(1), None)
        self.assertEqual(self.table.search(2), 'two')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
