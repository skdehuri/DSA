class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"[{self.value}|{'NODE' if self.next else 'NONE'}]"


class LinkedList:
    def __init__(self) -> None:
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
            print('LinkedList is empty')
            return
        
        current_node = self.head
        ll_str = ''

        while current_node:
            ll_str += str(current_node) + '-->  '
            current_node = current_node.next
        
        print(ll_str)
        

ll = LinkedList()

ll.print() # it should print LinkedList is empty

ll.append(5)
ll.append(4)
ll.append(8)

ll.extend([1, 2, 3, 4])

ll.print()


