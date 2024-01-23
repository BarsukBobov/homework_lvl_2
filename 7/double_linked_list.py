# двусвязный список

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node_to_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.tail = node
        else:
            self.head.previous = node
            node.next = self.head
        self.head = node

    def remove_node_from_begin(self):
        if self.head:
            if next_node := self.head.next:
                next_node.prev = None
            self.head = next_node
        else:
            raise ("пустой двухсвязный список")

    def add_node_to_end(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def remove_node_from_end(self):
        if self.tail:
            if prev_node := self.tail.prev:
                prev_node.next = None
            self.tail = prev_node
        else:
            raise ("пустой двухсвязный список")

    def get_node_from_begin(self):
        return self.head.data

    def get_node_from_end(self):
        return self.tail.data


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.add_node_to_begin(1)
    linked_list.add_node_to_begin(100)
    print(linked_list.get_node_from_begin())
    linked_list.remove_node_from_begin()
    linked_list.add_node_to_end(4)
    linked_list.remove_node_from_end()
    print(linked_list.get_node_from_end())
