'''

LeetCode :> https://leetcode.com/problems/sort-list/description/
Coding Ninja :> https://www.naukri.com/code360/problems/sort-linked-list_920517?interviewProblemRedirection=true&search=sort%20link
Problem Statement: Given the head of a linked list, return the list after sorting it in ascending order.
Example :
Input: head = [4,2,1,3]
Output: [1,2,3,4]

🚨🚨🚨🚨🚨🚨 Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)? 🚨🚨🚨🚨🚨🚨🚨
'''

# Brute Force / NeetCode 
from turtle import right


def sortLi(self,head):
    
    # Edge Case 
    if head is None or head.next is None :
        return head 
    
    left = head 
    right = self.getMid(head)
    temp = right.next 
    right.next = None 
    right = temp 
    
    
    left = self.sortLi(left)
    right = self.sortLi(right)
    
    return self.merge(left,right)


def getMid(self,head):
    if head is None or head.next is None : 
        return head 
    
    slow = head 
    fast = head 
    
    while fast.next is not None and fast.next.next is not None :
        slow = slow.next 
        fast = fast.next.next 
    return slow


def merge(self,left,right):
    tail = dummy = ListNode() 
    
    while left and right :
        if left.val < right.val :
            tail.next = left
            left = left.next 
        else :
            tail.next = right 
            right = right.next 
        tail = tail.next
        
        if left :
            tail.next = left 
        if right :
            tail.next = right
    return dummy.next