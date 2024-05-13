'''
GFG :> https://www.geeksforgeeks.org/problems/find-length-of-loop/1

Given a linked list of size N. The task is to complete the function countNodesinLoop() that checks whether a given Linked List contains a loop or not and if the loop is present then return the count of nodes in a loop or else return 0. C is the position of the node to which the last node is connected. If it is 0 then no loop.

'''

def countNodes (head):
    
    if head is None or head.next is None :
        return 0 
    
    tori = head 
    hari = head 
    
    while hari and hari.next :
        
        tori = tori.next 
        hari = hari.next.next 
        
        if tori == hari :
            count = 1
            current = hari.next 
            
            while current != tori:
                current = current.next
                count += 1
            return count 
    
    return 0