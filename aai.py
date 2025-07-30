class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Solution:
    def insertAtEnd(self, head, x):
        new_node = Node(x)
        
        # If the linked list is empty, return new node as head
        if head is None:
            return new_node
        
        current = head
        # Traverse till the last node
        while current.next is not None:
            current = current.next
        
        # Append the new node at the end
        current.next = new_node
        
        return head

