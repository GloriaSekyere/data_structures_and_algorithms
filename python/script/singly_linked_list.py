# sll Node
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head: SLLNode | None = None

    def append(self, data):
        new_node = SLLNode(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")

    def find(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def insert(self, position: int, data):
        insert_node = SLLNode(data)

        if position <= 0:
            insert_node.next = self.head
            self.head = insert_node
            return

        current_node = self.head
        current_index = 0

        while current_node and (current_index < position - 1):
            current_node = current_node.next
            current_index += 1

        if current_node:
            insert_node.next = current_node.next
            current_node.next = insert_node
        else:
            self.append(data)

    def remove(self, target):
        if not self.head:
            return False

        if self.head and (self.head.data == target):
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == target:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def get_min(self):
        if not self.head:
            return None

        lowest = float("inf")
        current = self.head
        while current:
            if current.data <= lowest:
                lowest = current.data
            current = current.next
        return lowest

    def get_max(self):
        if not self.head:
            return None

        highest = -float("inf")
        current = self.head
        while current:
            if current.data > highest:
                highest = current.data
            current = current.next
        return highest

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
