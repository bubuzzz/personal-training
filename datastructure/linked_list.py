
class LinkedListNode:
    def __init__(self, prev, value):
        self.value = value
        self.prev = prev

    def __str__(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        if self.head == None:
            current = LinkedListNode(None, value)
            self.head = current
        else:
            current = LinkedListNode(self.tail, value)

        self.tail = current
        self.size = self.size + 1

    def add_first(self, value):
        current = LinkedListNode(None, value)
        if self.head is not None:
            self.head.prev = current

        self.head = current
        self.size = self.size + 1

    def add_last(self, value):
        current = LinkedListNode(self.tail, value)
        self.tail = current
        self.size = self.size + 1

    def add_all(self, elements=[]):
        for el in elements:
            self.add(el)
        self.size = self.size + len(elements)

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

    def get(self, index):
        pass

    def remove(self):
        return self.head

    def __str__(self):
        current = self.tail
        result = ""

        if current != None:
            while current.prev != None:
                result = result + " " + str(current.value)
                current = current.prev
            result = result + " " + str(self.head.value)

        return result

import unittest

class TestLinkedList(unittest.TestCase):
    def test_add_first(self):
        a = LinkedList()
        a.add_first(0)
        self.assertEqual(a.size, 1)

    def test_add_first(self):
        a = LinkedList()
        a.add_first(0)
        a.add_last(0)
        self.assertEqual(a.size, 2)

    def test_clear(self):
        a = LinkedList()
        a.add_first(0)
        a.add_last(0)

        self.assertEqual(a.size, 2)
        a.clear()
        self.assertEqual(a.size, 0)

    def test_add_all(self):
        b = LinkedList()
        b.add_all([10, "20", 30])
        self.assertEqual(b.size, 3)

if __name__ == '__main__':
    unittest.main()

