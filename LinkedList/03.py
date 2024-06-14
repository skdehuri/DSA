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

    def length(self):

        if not self.head:
            return 0
        
        current_node = self.head
        count = 0

        while current_node:
            count += 1
            current_node = current_node.next

        return count

    def append(self, value):

        if not self.head:
            self.head = Node(value)
            return
        
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(value)

    def remove_from_beginning(self):

        if not self.head:
            print("LinkedList is empty")
            return
        
        self.head = self.head.next

    def remove_from_end(self):

        if not self.head:
            print("LinkedList is empty")
            return
        
        current_node = self.head

        if not self.head.next:
            self.head = None
            return

        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def remove_based_on_index(self, index):

        if not self.head:
            print("LinkedList is empty")
            return
        
        current_node = self.head
        count = 0

        while current_node.next:
            if count == index - 1:
                current_node.next = current_node.next.next
                break
            count += 1
            current_node = current_node.next

    def remove_from_middle(self):

        if not self.head:
            print("LinkedList is empty")
            return
        
        index = self.length() // 2
        print('index >> ',index)

        self.remove_based_on_index(index)



ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

ll.print()

ll.remove_from_beginning()
ll.print()

ll.remove_from_end()
ll.print()

ll.remove_from_end()
ll.print()

ll.remove_from_end()
ll.print()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.print()
ll.remove_based_on_index(2)
ll.print()
ll.append(6)

ll.print()
ll.remove_from_middle()
ll.print()
