# Stack implementation with Singly Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        removed_node = self.head
        self.head = self.head.next
        self.size -= 1
        return removed_node.data

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.data

    def isEmpty(self):
        return self.head == None

    def stack_size(self):
        return self.size


# Stack implementation with Python list

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, data):
#         self.stack.append(data)

#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack.pop()

#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack[-1]

#     def isEmpty(self):
#         return len(self.stack) == 0

#     def size(self):
#         return len(self.stack)
