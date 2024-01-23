# односвязный список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node_to_begin(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def remove_node_from_begin(self):
        if self.head:
            self.head = self.head.next
        else:
            raise ("пустой список")

    def get_node_from_begin(self):
        return self.head.data


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_node_to_begin(1)
    linked_list.add_node_to_begin(100)
    linked_list.add_node_to_begin(1000)
    linked_list.remove_node_from_begin()
    print(linked_list.get_node_from_begin())
