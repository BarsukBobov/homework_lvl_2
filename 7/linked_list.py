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

    def add_node_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def add_node_to_n(self, data, n):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        if n == 0:
            self.add_node_to_begin(data)
            return
        current = self.head
        i = 0
        while i < n:
            i += 1
            prev = current
            try:
                current = current.next
            except:
                print(f"Нельзя вставить элемент с порядковым номером {n}. "
                      f"Максимальное значение n для этого списка {i - 1}!")
                return
        prev.next = new_node
        new_node.next = current

    def remove_node_from_begin(self):
        if self.head:
            self.head = self.head.next
        else:
            raise ("пустой список")

    def get_node_from_begin(self):
        return self.head.data

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_node_to_begin(1)
    linked_list.add_node_to_begin(100)
    linked_list.add_node_to_begin(1000)
    linked_list.remove_node_from_begin()
    linked_list.get_node_from_begin()
    linked_list.add_node_to_n(500, 3)
    linked_list.printList()
