class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"|{self.value}|"
    

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):

        if not self.head:
            self.head = Node(value)
            return
        
        self.head = Node(value, self.head)

    def print(self):

        if not self.head:
            print("Stack is Empty")
            return
        
        current_node = self.head
        stack_str = ''

        while current_node:
            stack_str += str(current_node) + '\n'
            current_node = current_node.next

        print(stack_str)

    def pop(self):
        
        if not self.head:
            print("Stack is empty")
            return
        
        self.head = self.head.next


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.print()

stack.pop()
stack.print()

stack.pop()
stack.print()
