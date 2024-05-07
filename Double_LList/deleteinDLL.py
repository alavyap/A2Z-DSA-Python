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
def deleteatK(head,k):
    if head is None  :
        return head
    if k == 1 :
        head = head.next
        head.next.prev = None 
        return head
    
    
    temp = head 
    
    count = 0
  
    while temp is not None :
        count += 1 
        temp = temp.next 
        
        if (count == k): 
            break
        
    back = temp.prev
    front = temp.next
    
    if (back == None and front == None):
        del(temp)
        return None
    
    elif (back == None):
        return deleteHead(head)
         
        
    elif (front == None):
        return deleteatTail(head)
         
    
    else :
        back.next = front 
        front.prev = back 
        temp.next = None 
        temp.prev = None 
        return head 
    
    
    
    
# Delete A given Node 
def deleteNode(head,el):
    
    if head is None or head.next is None:
        return None
    
    temp = head 
    
    while (temp != None):
        temp = temp.next 
        
        if temp.value == el :
            