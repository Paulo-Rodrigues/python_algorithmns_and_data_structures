import unittest
from singly_linked_list import SinglyLinkedList, Node

class NodeTest(unittest.TestCase):
    def setUp(self):
        self.node = Node(1)

    def test_init(self):
        self.assertEqual(self.node.data, 1)
        self.assertEqual(self.node.next, None)

    def test_set_data(self):
        self.node.data = 2
        self.assertEqual(self.node.data, 2)

    def test_set_next(self):
        self.node.next = Node(3)
        self.assertEqual(self.node.next.data, 3)

    def test_get_data(self):
        self.assertEqual(self.node.data, 1)

    def test_get_next(self):
        self.node.next = Node(3)
        self.assertEqual(self.node.next.data, 3)

class SinglyLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.sll = SinglyLinkedList()

    def test_add_node(self):
        self.sll.add_node(1)
        self.assertEqual(self.sll.head.data, 1)
        self.assertEqual(self.sll.tail.data, 1)
        self.assertEqual(self.sll.size, 1)

    def test_remove_node(self):
        self.sll.add_node(1)
        self.sll.add_node(2)
        self.sll.add_node(3)
        self.sll.remove_node(self.sll.head)
        self.assertEqual(self.sll.head.data, 2)
        self.assertEqual(self.sll.tail.data, 3)
        self.assertEqual(self.sll.size, 2) 

if __name__ == '__main__':
    unittest.main()