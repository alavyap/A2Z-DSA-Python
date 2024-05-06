'''
Coding Ninja :> https://www.naukri.com/code360/problems/insert-at-end-of-doubly-linked-list_8160464?leftPanelTabValue=SOLUTION
Problem statement
A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have reference to both the previous and the next nodes in the sequence of nodes.
Given a doubly-linked list and a value ‘k’, insert a node having value ‘k’ at the end of the doubly linked list.

Note:
You need not print anything. You’re given the head of the linked list. Return the head of the modified list.
Example:
Input: Linked List: 4 <-> 10 <-> 3 <-> 5 and ‘k’ = 20

Output: Modified Linked List: 4 <-> 10 <-> 3 <-> 5 <-> 20

Explanation: A new node having value ‘k’ = 20 is inserted at the end of the linked list.

'''

class Node: 
    def __init__ (self, value):
        self.value = value
        self.next = None
        self.prev = None
        
        
#  Insertion on the Last Node   
def insertAtTail(head,k):
    
    if head is None :
        return Node(k)
    
    temp = head
    
    while (temp.next != None):
        temp = temp.next

    newNode = Node(k)
    temp.next = newNode
    newNode.prev = temp
    return head
         