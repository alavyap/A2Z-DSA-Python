'''
Coding Ninja :> https://www.naukri.com/code360/problems/middle-of-linked-list_973250
LeetCode :> https://leetcode.com/problems/middle-of-the-linked-list/description/

Problem Statement: Given the head of a linked list of integers, determine the middle node of the linked list. However, if the linked list has an even number of nodes, return the second middle node.

Example :
Input: LL: 1  2  3  4  5 
Output: 3
Explanation: Node with value 3 is the middle node of this linked list.
'''

class Node :
    def __init__ (self,value):
        self.value = value 
        self.next = None

# Brute Force 
def findMid(head):
    
    if head is None or head.next is None :
        return head 
    
    
    temp = head 
    count = 0 
    
    while(temp != None):
        count += 1
        temp = temp.next 
        
        
    mid = (count // 2 ) + 1
    
    temp = head
    
    while (temp != None) :
        
        mid -= 1 
        
        if mid == 0 :
            break 
        temp = temp.next 
        
    return temp
    
    
# Optimal Code 
def secondMid(head):
    
    if head is None or head.next is None :
        return head 
    
    tor = head 
    hare = head
    
    while(hare is not None and hare.next is not None):
        tor = tor.next 
        hare = hare.next.next
        
    return tor
    