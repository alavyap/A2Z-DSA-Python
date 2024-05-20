'''
LeetCode :> https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

Problem Statement: You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Example :
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
''' 

# Brute Force 
def midDelete(head):
    if head is None or head.next is None :
        return head 
    
    temp = head 
    count = 0 
    
    while temp:
        count += 1 
        temp = temp.next 
    dele = count // 2 
    temp = head 
    prev = None 
    
    for i in range (dele):
        prev = temp 
        temp = temp.next 
    if prev  is not None:
        prev.next = temp.next
    return head 

# Optimal Approach 
def deleteMiddle(head):
    
    # Edge Case 
    if head is None or head.next is None:
        return head 
    
    hari = tori = head 
    prev = None 
    
    while hari and hari.next :
        prev = tori 
        tori = tori.next 
        hari = hari.next.next 
        
    if prev is not None :
        prev.next = tori.next 
    return head 