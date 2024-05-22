'''
Coding Ninjas :> https://www.naukri.com/code360/problems/sort-linked-list-of-0s-1s-2s_1071937?interviewProblemRedirection=true&search=Linked%20List
GFG :> https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

Problem statement
Given a linked list of 'N' nodes, where each node has an integer value that can be 0, 1, or 2. You need to sort the linked list in non-decreasing order and the return the head of the sorted list.

Example:
Given linked list is 1 -> 0 -> 2 -> 1 -> 2. 
The sorted list for the given linked list will be 0 -> 1 -> 1 -> 2 -> 2.

'''

# Optimal Approach 

def sorti(head):
    
    if head is None or head.next is None: 
        return head 
    
    count = [0,0,0]
    temp = head 
    while temp :
        count[temp.data] += 1
        temp = temp.next 
    
    temp = head
    for i in range (3):
        while count[i] > 0:
            temp.data = i 
            temp = temp.next 
            count[i] -= 1 
    return head 

'''
Follow Up:
Can you solve this without updating the Nodes of the given linked list?
'''
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def sortWithoutSpace(head):
    
    if head is None or head.next is None :
        return head 
    
    # Dummy Nodes for lists of 0s,1s,2s
    zeroD = Node(0)
    oneD = Node(0)
    twoD = Node(0)
    
    # Current Pointer for 3 lists 
    zero = zeroD 
    one = oneD 
    two = twoD 
    
    # Traverse the list and distribute the nodes into the three lists
    
    temp = head 
    
    while temp : 
        if temp.data == 0 :
            zero.next = temp 
            zero = zero.next 
            
        elif temp.data == 1 :
            one.next = temp 
            one = one.next 
            
        else:
            two.next = temp 
            two = two.next 
            
        temp = temp.next 
        
        
    # Connect the three lists 
    zero.next = oneD.next if oneD.next else twoD.next
    
    one.next = twoD.next 
    two.next = None 
    
    return zeroD.next