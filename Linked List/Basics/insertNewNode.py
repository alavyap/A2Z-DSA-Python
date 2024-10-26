'''
Coding Ninja :> https://www.naukri.com/code360/problems/insert-node-at-the-beginning_8144739
Problem statement
You are given the head of a linked list ‘list’ of size ‘N’ and an integer ‘newValue’.
Your task is to insert a node with the value ‘newValue’ at the beginning of the ‘list’ and return the new head of the linked list.
You must write an algorithm whose time complexity is O(1) and whose space complexity is O(1).
Note:
In the output, you will see the elements of the linked list made by you.
Example:
Input: ‘N’ = 4, ‘newValue’ = 0
‘list’ = 4 -> 2 -> 5 -> 1
Output: 0 4 2 5 1
Explanation: Linked List after inserting the newValue is 0 -> 4 -> 2 -> 5 -> 1.
'''

class Node:
    def __init__(self,value):
        self.value = value 
        self.data = None 
        

# Coding Ninja Solution
def insertAtFirst(list: Node, newValue: int) -> Node:
    # Write your code here
    temp = Node(newValue)
    temp.next = list  
    return temp

# Insertion form the last 
def insertionAtLast(list,newValue):
    # Edge Case 
    if list is None :
        return  Node(newValue)
    temp = list 
    
    while (temp.next != None):
        temp = temp.next  
        
    newNode = Node(newValue)
    temp.next = newNode
    return list

'''
Inserting at a given Kth element/poistion
 K will be ranging between (1 to N +1) 
 N is the length of the linked list 
'''

def insertionAtK (list,newValue,k):
    if list is None :
        if (k == 1 ):
            return Node(newValue)
        else:
            return list 
        
    if (k == 1):
        return Node(newValue,list) 
    
    count = 0 
    temp = list 
    while (temp != None):
        count += 1 
        if (count == k):
            x = Node(newValue,temp.next)
            temp.next = x 
            break
        
        temp = temp.next  
    return list


# Inserting a Value in the linked list


def insertionAtPosition (list,newValue,val):
    if list is None :
        return None
        
    if (list.data == val):
        return Node(newValue,list) 
    
    
    temp = list 
    while (temp.next != None):
        
        if (temp.next.data == val):
            x = Node(newValue)
            x.next = temp.next
            temp.next = x 
            break
        
        temp = temp.next  
    return list
