class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        count = 1
        c_node = self.head
        while c_node is not None:
            c_node = c_node.next
            count += 1
        return count

    def append(self, data):
        node = Node(data)
        self.tail.next = node
        self.tail = node

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
