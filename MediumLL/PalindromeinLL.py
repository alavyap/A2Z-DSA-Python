'''
Coding Ninja :> https://www.naukri.com/code360/problems/palindrom-linked-list_799352?interviewProblemRedirection=true&search=Linked%20List
LeetCode :>  https://leetcode.com/problems/palindrome-linked-list/description/

Problem statement
You are given a singly Linked List of integers. Your task is to return true if the given singly linked list is a palindrome otherwise returns false.

For example:
The given linked list is 1 -> 2 -> 3 -> 2-> 1-> NULL.
It is a palindrome linked list because the given linked list has the same order of elements when traversed forwards and backward​.
Follow Up:
Can you solve the problem in O(N) time complexity and O(1) space complexity iteratively?


'''
# Brute Force 
from collections import deque


def pali (head):
  
    stacki = deque()
    temp = head 
    while temp is not None :
        stacki.append(temp.data)
        
        temp = temp.next 
    
    # Checking Palindrome 
    temp  = head 
    while temp != None :
        if temp.data != stacki.pop():
            return False 
        temp = temp.next 
        
    return True 

# Time Complexity of this code is O(2*N)
# Space Complexity of this code is O(N)
    


#Better Approach

def isPali(head):
    
    # Edge Case 
    if head is None or head.next is None : 
        return True 
    
    hari = head 
    tori = head 
    
    while hari.next is not  None and hari.next.next is not  None :
        tori = tori.next 
        hari = hari.next.next 
        
    new_head = reverseRecursion(tori.next)
    
    first = head 
    second = new_head
    
    while second is not None :
        if first.data != second.data: 
            reverseRecursion(new_head)
            
            return False
        
        first = first.next 
        second = second.next 
    reverseRecursion(new_head)
    return True

def reverseRecursion(head):
    if head is None or head.next is None :
        return head 
    
    new_head = reverseRecursion(head.next)
    
    front = head.next 
    front.next = head 
    head.next = None  
    
    return new_head
    
    
'''
Every Linked List Problem, if you can't do it in LinkedList format,
copy the data in list and now your question would become for an 
array, solve it.
'''

# Optimal Approach

def isPalindrome(head):
    if not head or not head.next :
        return True 
    
    slow = head 
    fast = head 
    reversed_list = None 
    
    while fast is not None and fast.next is not None :
        tmp = slow 
        
        slow = slow.next 
        fast = fast.next.next 
        
        
        tmp.next = reversed_list 
        reversed_list = tmp 
        
        
    if fast is not None :
        slow = slow.next 
            
    while reversed_list is not None and reversed_list.val == slow.val :
        reversed_list = reversed_list.next 
        slow = slow.next 
    return reversed_list is None 

# T: O(N)
# S : O(1)