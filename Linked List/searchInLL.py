'''
Coding Ninja :> https://www.naukri.com/code360/problems/search-in-a-linked-list_975381

You are given a Singly Linked List of integers with a head pointer. Every node of the Linked List has a value written on it.
A sample Linked List:
Now you have been given an integer value, 'K'. Your task is to check whether a node with a value equal to 'K' exists in the given linked list. Return 1 if node exists else return 0.
'''

class Node :
    def __init__(self,value) -> None:
        self.value = value 
        self.next = None
        
        
def searchLL(head,k):
    if head is None:
        return 0
    temp = head 
    while (temp != None):
        if temp.value == k :
            return 1 
        temp = temp.next 
        
    return 0