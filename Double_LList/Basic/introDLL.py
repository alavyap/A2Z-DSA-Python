'''
Coding Ninja :> https://www.naukri.com/code360/problems/introduction-to-doubly-linked-list_8160413

Problem statement
You are given an array ‘Arr’ of size ‘N’ consisting of positive integers.
Your task is to make a doubly linked list from the array and return the head of the linked list.
Here, the head of the doubly linked list is the first element of the array, and the tail of the doubly linked list is the last element.
Note:
A doubly linked list is one in which it is possible to access the next and the previous nodes from a node in the linked list (if they exist).

Example:
Input: ‘N’ = 4, ‘Arr’ = [4, 2, 5, 1]
Output: 4 2 5 1
Explanation: Doubly Linked List for the array ‘Arr’ = [4, 2, 5, 1] is 4 <-> 2 <-> 5 <-> 1.

'''

# Code for basic Node 
class Node :
    def __init__(self,value) :
        self.value = value 
        self.prev = None 
        self.next = None
        
# Construction of Doubly Linked List 
def constructDLL(arr):
    if not  arr:
        return None
    
    head = Node(arr[0])
    temp = head 
    
    for i in range (1,len(arr)):
        newNode = Node(arr[i])
        temp.next = newNode
        newNode.prev = temp 
        temp = newNode
    return head