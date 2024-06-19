class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"[{self.value}|{'NODE' if self.next else 'NULL'}]"
    
class LinkedList:
    def __init__(self):
        self.head = None

    def add_values(self, values):

        def add(value):
            if not self.head:
                self.head = Node(value)
                return
            
            current_node = self.head

            while current_node.next:
                current_node = current_node.next
            
            current_node.next = Node(value)
        
        for value in values:
            add(value)
        
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

    def rotate_right(self, k=1):
        
        if not self.head:
            print("Linkedlist is empty")
            return
        
        tail_node = self.head
        ll_length = 1

        while tail_node.next:
            ll_length += 1
            tail_node = tail_node.next

        # remove extra rotations
        k = k % ll_length

        count = 0
        current_node = self.head

        # loop till we get the node where we need to modify the linkedlist structure
        while count != (ll_length - k - 1):
            count += 1
            current_node = current_node.next
        
        tail_node.next = self.head
        self.head = current_node.next
        current_node.next = None

    def rotate_left(self, k=1):

        if not self.head:
            print("Linkedlist is empty")
            return
        
        tail_node = self.head
        ll_length = 1

        while tail_node.next:
            ll_length += 1
            tail_node = tail_node.next
        
        k = k % ll_length
        current_node = self.head
        count = 1

        while count != k:
            count += 1
            current_node = current_node.next

        temp_node = current_node.next
        current_node.next = None
        tail_node.next = self.head
        self.head = temp_node


ll = LinkedList()
ll.add_values([1, 2, 3, 4, 5, 6, 7, 8])
ll.print()

ll.rotate_right()
ll.print()

ll.rotate_right(3)
ll.print()

ll.rotate_left()
ll.rotate_left(3)
ll.print()