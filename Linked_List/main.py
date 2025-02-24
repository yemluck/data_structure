"""
To build a linked list.
We need 2 classes
1. The node
2. The linked list

Linked list would have the following operations
1. append at end
2. prepend at the beginning
3. Traverse through the linked list
4. Insert into the linked list at an index
5. Print the linked list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the beginning of a linked list
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head # Note, always care for the pointer i.e. next before caring for the node
            self.head = new_node

    # Insert a node at a specific position in a linked list
    def insert_at_index(self, data, index):
        if index == 0:
            self.prepend(data) # if index is 0, it means to prepend the new node

        position = 0
        curr = self.head
        while curr is not None and position+1 != index:
            curr = curr.next
            position += 1

        if curr.next is not None:
            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node
        else:
            print("Index not present")

    # insert a node at the end of a linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next: # this loop will run till it gets to the end of the linked list where curr.next is None
                curr = curr.next
            curr.next = new_node # at the end of the loop, we point the pointer to the new node


    # Method to update node at a given position
    def update_node(self, data, index):
        curr = self.head
        position = 0

        while curr is not None and position != index:
            curr = curr.next
            position += 1

        if curr is not None:
            curr.data = data
        else:
            print("Index not present")







    def print_list(self):
        output = []

        if self.head is None:
            print("Empty")
        else:
            curr = self.head
            while curr:
                output.append(curr.data)
                curr = curr.next
            print(output)
            print(len(output))




my_linked_list = LinkedList()
my_linked_list.append(3)
my_linked_list.append(5)
my_linked_list.append(9)
my_linked_list.print_list()


