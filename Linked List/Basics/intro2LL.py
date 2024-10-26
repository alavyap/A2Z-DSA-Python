'''
Coding Ninja :> https://www.naukri.com/code360/problems/introduction-to-linked-list_8144737
Problem statement
You are given an array ‘Arr’ of size ‘N’ consisting of positive integers.
Make a linked list from the array and return the head of the linked list.
The head of the linked list is the first element of the array, and the tail of the linked list is the last element.
Note:
In the output, you will see the elements of the linked list made by you.
Example:
Input: ‘Arr’ = [4, 2, 5, 1]
Output: 4 2 5 1
Explanation: Linked List for the array ‘Arr’ = [4, 2, 5, 1] is 4 -> 2 -> 5 -> 1.
'''
class Node :
    def __init__(self,value) :
        self.value = value
        self.next = None
        
def constructLL(arr):
    if not arr: 
        return None 
    
    head = Node(arr[0])
    tail = head
    
    for i in range (1,len(arr)):
        newNode = Node(arr[i])
        tail.next = newNode
        tail = newNode
        
    return head
# Test Run 
 
print(constructLL([4,2,3,5,1]))
# constructLL([4,2,3,5,1])