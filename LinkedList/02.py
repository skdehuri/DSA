class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"[{self.value}|{'NODE' if self.next else 'NULL'}]"


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):

        if not self.head:
            print("LinkedList is empty")
            return
        
        current_node = self.head
        ll_str = ''

        while current_node:
            ll_str += str(current_node) + ' ----> '
            current_node = current_node.next

        print(ll_str)

    def prepend(self, value):

        if not self.head:
            self.head = Node(value)
            return
        
        current_node = self.head
        self.head = Node(value, current_node)
    
    def append(self, value):

        if not self.head:
            self.head = Node(value)
            return
        
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(value)

    def length(self):

        if not self.head:
            return 0
        
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next

        return count
    
    def insert_based_on_index(self, index, value):

        if not self.head:
            self.head = Node(value)
            return
        
        current_node = self.head
        count = 0

        while current_node.next:
            if count == index - 1:
                next_node = current_node.next
                current_node.next = Node(value, next_node)
                break
            count += 1
            current_node = current_node.next

    def insert_at_middle(self, value):

        if not self.head:
            self.head = Node(value)
            return
        
        middle_index = self.length() // 2
        self.insert_based_on_index(middle_index + 1, value)

    def insert_after_value(self, check_value, value):

        if not self.head:
            self.head = Node(value)
            return
        
        current_node = self.head

        while current_node.next:
            if current_node.value == check_value:
                next_node = current_node.next
                current_node.next = Node(value, next_node)
                break
            current_node = current_node.next


ll = LinkedList()

ll.append(3)

ll.print()

ll.prepend(2)
ll.prepend(1)

ll.append(4)

ll.print()

ll.append(5)

ll.print()

ll.insert_at_middle(999)

ll.print()

ll.insert_after_value(999, 888)
ll.print()