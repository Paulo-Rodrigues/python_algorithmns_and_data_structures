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

    def search(self, data):
      node = self.head
      while node is not None:
          if node.data == data:
              return node
          node = node.next
      return None
