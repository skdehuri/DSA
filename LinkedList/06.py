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

    def detect_loop(self, detection_type=1, remove_loop=False):
        if detection_type == 1:
            self.detect_loop_type_1(remove_loop)
        elif detection_type == 2:
            self.detect_loop_type_2(remove_loop)

    def detect_loop_type_1(self, remove_loop=False):
        
        if not self.head:
            print("Linkedlist is empty")
            return
        
        nodes = set()

        current_node = self.head
        prev_node = None

        while current_node.next:
            if current_node in nodes:
                print("loop detected")
                print(f"{prev_node} ---- + ---- {current_node}")
                if remove_loop:
                    prev_node.next = None
                    print("loop node removed")
                return
            nodes.add(current_node)
            prev_node = current_node
            current_node = current_node.next

        print("There is no loop in Linkedlist")


    def detect_loop_type_2(self, remove_loop=False):

        if not self.head:
            print("Linkedlist is empty")
            return
        
        slow_node = self.head
        fast_node = self.head
        loop_detected = False

        while slow_node and fast_node and fast_node.next:
            print('SLOW NODE - ', str(slow_node))
            print('FAST NODE - ', str(fast_node))

            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node == fast_node:
                loop_detected = True
                print("Loop Detected")
                break

        if not loop_detected:
            print("There is no loop in Linkedlist")
            return

        fast_node = self.head
        prev_node = None

        while slow_node != fast_node:
            print('SLOW NODE - ', str(slow_node))
            print('FAST NODE - ', str(fast_node))

            prev_node = slow_node
            slow_node = slow_node.next
            fast_node = fast_node.next
        
        print(f"Loop detection point ----> {prev_node} ---- + ---- {slow_node}")
        if remove_loop:
            print("Removing loop node")
            prev_node.next = None
            print("Loop node removed")


ll = LinkedList()
ll.add_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

ll.print()
ll.detect_loop()

ll.head.next.next.next.next.next.next.next.next.next.next = ll.head.next.next

ll.detect_loop()
ll.detect_loop(remove_loop=True)
ll.detect_loop()
ll.print()

ll.detect_loop(2)
ll.print()

ll.head.next.next.next.next.next.next.next.next.next.next = ll.head.next.next

ll.detect_loop(2)
ll.detect_loop(2, remove_loop=True)
ll.detect_loop(2)
ll.print()