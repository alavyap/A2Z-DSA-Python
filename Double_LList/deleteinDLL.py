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
    
# Striver Code 
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

# Deletion on the Head 
def deleteHead(head):
    if head is None  or head.next is None :
        return None 
    
    temp = head 
    
    head = head.next 
    
    head.prev = None
    temp.next = None
    
    return head 


# Delete at Kth Position
def deleteNode(self,head, position):
    # Code here
    if head is None or position <= 0:
        return

    current = head
    count = 1

    # Traverse to the node at the given position
    while current and count < position:
        current = current.next
        count += 1

    # If position is greater than the number of nodes
    if current is None:
        return

    # If the node to be deleted is the head node
    if current == head:
        head = current.next
        if head:
            head.prev = None
        return

    # If the node to be deleted is not the last node
    if current.next:
        current.next.prev = current.prev

    # If the node to be deleted is not the first node
    if current.prev:
        current.prev.next = current.next

    current = None
    
    
    
# Delete A given Node 
# Node can't be head

def deleteNode(el):
    
    back = el.prev
    front = el.next 
   
    if front == None :
       back.next = None 
       el.prev = None 
       return 
    
    back.next = front 
    front.prev = back 
    
    el.next = None 
    el.prev = None 
   