'''
Coding Ninja :> 
LeetCode :> 
Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example :
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

'''
# Brute Force 

def oddEven(head):
    
    
    # if head is None or head.next is None :
    if not head : 
        return head 
    
    odd = head 
    even = head.next 
    headEven = even 
    
    while (even and odd and even.head and odd.next):
        odd.next = even.next 
        odd = odd.next 
        even.next = odd.next 
        even = headEven 
    odd.next = headEven 
    return head 