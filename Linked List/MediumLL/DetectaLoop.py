'''
LeetCode :>  https://leetcode.com/problems/linked-list-cycle/description/ 
Coding Ninjas :> https://www.naukri.com/code360/problems/cycle-detection-in-a-singly-linked-list_628974?count=25&page=1&search=Linked%20List&sort_entity=order&sort_order=ASC&leftPanelTabValue=PROBLEM&customSource=studio_nav
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example :

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

'''

# Brute Force 
# from typing import DefaultDict


def possiCycle(head):
    if head is None or head.next is None:
        return False 
    
    temp = head 
    dicti = set()
    
    
    while temp != None :
        if temp in dicti :
            return True 
        dicti.add(temp) 
        temp = temp.next 
    return False

# Optimal Code 

def hasCycle(head):
    
    # Edge Case 
    if head is None or head.next is None :
        return False 
    tor = head 
    hare = head 
    
    while tor and hare and hare.next:
        tor = tor.next 
        hare = hare.next.next 
        
        if hare == tor :
            return True 
        
    return False