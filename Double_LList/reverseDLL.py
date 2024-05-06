'''
Coding Ninja :> https://www.naukri.com/code360/problems/reverse-a-doubly-linked-list_1116098
Problem statement
You are given a doubly-linked list of size 'N', consisting of positive integers. Now your task is to reverse it and return the head of the modified list.
Note:
A doubly linked list is a kind of linked list that is bidirectional, meaning it can be traversed in both forward and backward directions.

Example:
Input: 
4
4 3 2 1
This means you have been given doubly linked list of size 4 = 4 <-> 3 <-> 2 <-> 1.
Output: 1 2 3 4
Explanation : This means after reversing the doubly linked list it becomes 1 <-> 2 <-> 3 <-> 4.
'''

class Node :
    def __init__(self,value) -> None:
        self.value = value 
        self.next = None 
        self.prev = None
        
        
def reverseDLL(head):
    if head is None or head.next is None:
        return None 
    
    temp = head 
    prev = None
    
    while temp :
        nextNode = temp.next 
        temp.next = prev 
        temp.prev = nextNode
        prev = temp 
        temp = nextNode
        
        
    return prev