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
    


# Optimal Approach 
def isPali(head):
    
    # Edge Case 
    if head is None or head.next is None : 
        return False 
    
    
'''
Every Linked List Problem, if you can't do it in LinkedList format,
copy the data in list and now your question would become for an 
array, solve it.
'''