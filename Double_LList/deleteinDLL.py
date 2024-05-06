'''
Coding Ninja :> https://www.naukri.com/code360/problems/delete-last-node-of-a-doubly-linked-list_8160469
Problem statement
A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have reference to both the previous and the next nodes in the sequence of nodes.
Given a doubly-linked list, delete the node at the end of the doubly linked list.

Note:
You need not print anything. You’re given the head of the linked list, just return the head of the modified list.

Example:
Input: Linked List:  4 <-> 10 <-> 3 <-> 5 <-> 20
Output: Modified Linked List: 4 <-> 10 <-> 3 <-> 5
Explanation: The last node having ‘data’ = 20 is removed from the linked list.
'''

class Node :
    def __init__(self,value) -> None:
        self.value = value 
        self.next = None
        self.prev = None
        
        
# Deletion on the last Node 
def deleteAtTail(head):
    if head is None  or head.next == None:
        return None
    
    temp = head 
    
    while (temp.next.next != None):
        temp = temp.next 
        
    temp.next = None 
    
    return head
    
# Striver Code code 
def deleteatTail(head):
    if head is None or head.next is None :
        return None 
    
    temp = head 
    
    while temp is not None :
        temp = temp.next 
    
    newTail = temp.prev 
    newTail.next = None 
    temp.prev = None 
    
    del(temp)
    return head