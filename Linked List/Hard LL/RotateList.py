'''
LeetCode :> https://leetcode.com/problems/rotate-list/description/
Coding Ninja :> https://www.naukri.com/code360/problems/rotate-linked-list_920454

Given the head of a linked list, rotate the list to the right by k places.
Example :
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
'''

# Brute Force 
def rotateRight(head,k):
    if head is None or head.next is None : 
        return head 
    
    for i in range (k):
        temp = head
        while  temp.next is not None : 
            temp = temp.next 
        end =temp.next 
        temp.next = None 
        end.next = head 
        head = end 
    return head 


# Optimal Approach 
def rightRotate(head,k):
    if not head :
        return head 
    last_node = head 
    len = 1  
    
    while last_node.next :
        last_node = last_node.next 
        len += 1
        
    k = k % len 
    last_node.next = head 
    
    temp = head 
    for i in range (len - k - 1):
        temp = temp.next 
    ans = temp.next 
    temp.next = None 
    return ans 