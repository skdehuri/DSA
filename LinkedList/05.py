class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"[{self.value}|{'NODE' if self.next else 'NULL'}]"
    

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):

        if not self.head:
            self.head = Node(value)
            return
        
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(value)

    def extend(self, values):
        for value in values:
            self.append(value)

    def print(self):

        if not self.head:
            print("Linkedlist is empty")
            return
        
        current_node = self.head
        ll_str = ''

        while current_node:
            ll_str += str(current_node) + ' ----> '
            current_node = current_node.next

        print(ll_str)

    def reverse(self):
        
        if not self.head:
            print("Linkedlist is empty")
            return
        
        current_node = self.head
        prev_node = None

        while current_node:
            temp_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp_node

        self.head = prev_node


ll = LinkedList()

ll.extend([1, 2, 3, 4, 5, 6])
ll.print()

ll.reverse()
ll.print()
