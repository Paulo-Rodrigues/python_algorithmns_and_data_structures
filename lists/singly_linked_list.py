import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return node

    def remove_node(self, node):
        if self.head is None:
            return
        if self.head == node:
            self.head = self.head.next
            self.size -= 1
            return
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr == node:
                prev.next = curr.next
                self.size -= 1
                return
            prev = curr
            curr = curr.next
        return

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