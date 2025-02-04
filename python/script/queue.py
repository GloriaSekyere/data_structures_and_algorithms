# qeueue implementation with python list
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# queue implementation with a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_queue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("null")

    def enqueue(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        removed_node = self.head
        self.head = self.head.next
        self.size -= 1
        if not self.head:
            self.tail = None
        return removed_node.data

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.head.data

    def isEmpty(self):
        return self.size == 0

    def queue_size(self):
        return self.size
