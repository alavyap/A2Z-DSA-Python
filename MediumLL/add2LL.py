'''
LeetCode :>  https://leetcode.com/problems/add-two-numbers/
Coding Ninja :> https://www.naukri.com/code360/problems/add-two-linked-lists_799487?interviewProblemRedirection=true&search=Linked%20List

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example :
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

'''
# Brute Force 
from MediumLL.SortLL import ListNode


def addTwoNumbers(l1,l2):
    
    # Edge Case 
    if not l1 or not l2 :
        return None
    
    head = ListNode()
    temp = head 
    carry = 0 
    
    while (l1 is not None or l2 is not None) or carry :
        sum = 0 
        
        if l1 is not None :
            sum += l1.val
            l1 = l1.next 
        if l2 is not None :
            sum += l2.val
            l2 = l2.next 
        sum += carry 
        carry = sum // 10 
        new_node = ListNode(sum % 10 )
        temp.next = new_node 
        temp = temp.next 
    return head.next 


def add_by_neetcode (l1,l2):
    
    head = ListNode()
    temp = head 
    carry = 0 
    
    while l1 or l2 or carry :
        
        val1 = l1.val if l1 else 0 
        val2 = l2.val if l2 else 0 
        
        # New Digit 
        val = val1 + val2 + carry 
        
        carry = val // 10 
        val = val % 10 
        temp.next = ListNode(val)
        
        #  Update Pontiers 
        temp = temp.next 
        l1 = l1.next if l1 else None 
        l2 = l2.next if l2 else None 
    return temp.next