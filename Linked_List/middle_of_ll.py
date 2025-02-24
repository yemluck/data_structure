"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            new_node.next = None
            curr.next = new_node

    def insert(self, data, index):
        new_node = Node(data)
        position = 0
        curr = self.head

        while curr is not None and position+1 != index:
            curr = curr.next
            position += 1

        if curr.next is not None:
            new_node.next = curr.next
            curr.next = new_node
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
            # print(len(output))



    def middle_of_ll(self):
        slow = fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data



chris_ll = LinkedList()

chris_ll.append(3)
chris_ll.append(4)
chris_ll.append(5)
chris_ll.prepend(7)
chris_ll.insert(2,2)
chris_ll.print_list()

print(chris_ll.middle_of_ll())