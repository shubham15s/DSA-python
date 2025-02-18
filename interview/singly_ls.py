"""
A singly linked list is a linear data structure where each element, known as a node, contains two parts:

Data: The value stored in the node.
Next: A reference (or pointer) to the next node in the sequence.
This structure allows for efficient insertion and deletion operations.

Defining a Singly Linked List in Python:

To implement a singly linked list in Python, we can create two classes:

Node: Represents each node in the list.
LinkedList: Manages the nodes and provides methods to manipulate the list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Example usage:
if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)

    print("Original Linked List:")
    llist.display()

    llist.reverse()

    print("Reversed Linked List:")
    llist.display()
