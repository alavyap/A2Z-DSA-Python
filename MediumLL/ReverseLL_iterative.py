'''
LeetCode :> https://leetcode.com/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example :
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

'''
# Brute Force with Stack in It 
def listReverse(head):
    
    if head is None or head.next is None :
        return head 
    
    temp = head 
    stack = [] 
    
    while temp  is not None :
        stack.append(temp.data)
        temp = temp.next 
        
        
    temp = head 
    
    while temp is not None :
        temp.data = stack.pop() 
        
        temp = temp.next 
        
    return head 




# Optimal Approach 
def reverseAList(head):
    
    # Edge Case 
    if head is None or head.next is None :
        return head 
    
    temp = head 
    newT = None 
    
    while temp is not None:
        newNode = temp.next 
        temp.next = newT 
        newT  = temp 
        temp  = newNode 
    return newT


# Reversing the Linked List with Recursion 

def reverseList (head):
    
    # Edge Case 
    if head is None or head.next is None : 
        return head 
    
    
    newNode = reverseList(head.next)
    
    front = head.next
    front.next = head 
    
    head.next = None 
    return newNode
    
    