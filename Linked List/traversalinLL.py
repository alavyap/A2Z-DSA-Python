'''
Coding Ninja :> https://www.naukri.com/code360/problems/count-nodes-of-linked-list_5884?leftPanelTabValue=PROBLEM
Problem statement
Given the head of a singly linked list of integers, find and return its length.
Example:
The length of the list is 4. Hence we return 4.
Note:
Exercise caution when dealing with edge cases, such as when the head is NULL. Failing to handle these edge cases appropriately may result in a runtime error in your code.


'''
class Node :
    def __init__(self,value):
        self.value = value 
        self.next = None
        
        
def traverseLL(head):
    if head is None:
        return 0
    temp = head 
    
    count = 0 
    
    while (temp != None):
        count += 1 
        temp = temp.next 
    return count


# Just traversing in a linked list 
def justTraversingLL(head):
    temp = head
    while temp is not None :
        print(temp.data,end= " -> ")
        temp = temp.next  
    print("None")