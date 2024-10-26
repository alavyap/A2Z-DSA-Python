'''
Coding Ninja :> https://www.naukri.com/code360/problems/delete-node-of-linked-list_8160463
LeetCode :> https://leetcode.com/problems/delete-node-in-a-linked-list/description/

There is a singly-linked list head and we want to delete a node node in it.
You are given the node to be deleted node. You will not be given access to the first node of head.
All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.
Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
Custom testing:

For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.
 
Example :
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

'''

# Coding Ninja > If the node is not given 

class Node :
    def __init__(self,value) :
        self.value = value 
        self.next = None 
        
        
def deleteLast (list):
    if list == None or list.next == None :
        return None
    temp = list 
    
    while (temp.next.next != None):
        temp = temp.next 
        
    temp.next = None 
    
    return list

# If the node is given  to delete
def deleteNode (list,k):
    
    # Base Case 
    if list is  None:
        return list
    
    # If K == 1 , i.e the first node of the linked list 
    if (k == 1) :
        list = list.next 
        return list
    
    temp = list 
    count = 0
    prev = None
        
    while (temp != None):
        count += 1 
        temp = temp.next 
            
        if (count == k) :
            prev.next = prev.next.next 
               
            break 
            
        prev = temp 
        temp = temp.next  
    return list


# If a value is given to delete 
def deletValue (list,el):
    if list is None :
        return None 
    if (list.value == el) :
        temp = list 
        return list 
    
    temp = list 
    prev = None
    
    while (temp != None):
        if temp.value == el :
                
            prev.next = prev.next.next 
            break 
        
        prev = temp
        temp = temp.next 
    return list    



# LeetCode  Solution 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

























def display_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Display the original linked list
print("Original Linked List:")
display_linked_list(head)

# Delete the node at position k (in this case, let's say k=3)
k = 3
head = deleteNode(head, k)

# Display the linked list after deletion
print("\nLinked List after deleting node at position", k, ":")
display_linked_list(head)