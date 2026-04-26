## Task 5 & 6: Singly Linked List with Extended Functions
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Task 5 Operations
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, data):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print(f"Element {data} not found.")

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return "Element found"
            current = current.next
        return "Element not found"

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    # Task 6 Extended Operations
    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


print("\n" + "=" * 45)
print("TASK 5: Singly Linked List")
print("=" * 45)

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
print("Linked List:")
ll.display()

ll.insert_at_beginning(5)
print("After inserting 5 at beginning:")
ll.display()

ll.delete_node(20)
print("After deleting 20:")
ll.display()

print("Search 30:", ll.search(30))
print("Search 99:", ll.search(99))


print("\n" + "=" * 45)
print("TASK 6: Extended Linked List Functions")
print("=" * 45)

ll2 = LinkedList()
for val in [10, 20, 30, 40]:
    ll2.insert_at_end(val)

print("Linked List:")
ll2.display()
print("Number of nodes:", ll2.count_nodes())
print("Middle element:", ll2.find_middle())

ll2.reverse_list()
print("Reversed list:")
ll2.display()

