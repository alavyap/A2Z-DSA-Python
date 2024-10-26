'''
LeetCode :> https://leetcode.com/problems/copy-list-with-random-pointer/description/
Coding Ninja :> https://www.naukri.com/code360/problems/clone-a-linked-list-with-random-pointers_983604
Problem statement: You are given a linked list containing 'n' nodes, where every node in the linked list contains two pointers:
(1) ‘next’ which points to the next node in the list

(2) ‘random’ which points to a random node in the list or 'null'.

Your task is to create a 'deep copy' of the given linked list and return its head.
Note:
A 'deep copy' of a linked list means we do not copy the references of the nodes of the original linked list, rather for each node in the original linked list, a new node is created.

Example :
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

'''

# Brute Force 
def copyRandom(head):
    temp = head 
    hash_M = {}
    
    while temp is not None :
        new_node = Node(temp.data) 
        hash_M[temp] = new_node
        
        temp = temp.next 
        
    temp = head 
    
    while temp is not None : 
        
        copy = hash_M[temp]
        
        copy.next = hash_M.get(temp.next)
        
        copy.random = hash_M.get(temp.random)
        
        temp = temp.next 
    return hash_M.get(head)        
        
        
# Optimal Approach 
def insert_Copy(head):
    temp = head 
    while temp :
        next_Element = temp.next 
        
        copy = Node(temp.data)
        
        copy.next = next_Element
        
        temp.next = copy 
        temp = next_Element
        
# Function to connect random 
def connect_Random (head):
    temp = head 
    while temp :
        copy = temp.next 
        if temp.random :
            copy.random = temp.random.next 
        else :
            copy.random = None 
            
        temp = temp.next.next 
        
# Function  to Copy 
def deepCopy (head):
    temp = head 
    dummy = Node(-1)
    
    result = dummy 
    
    while temp :
        
        result.next = temp.next 
        result = result.next 
        
        temp.next = temp.next.next 
        temp = temp.next 

    return dummy.next


# Main Function
def cloneLL(head):
    if not head :
        return None 
    
    insert_Copy(head)
    connect_Random(head)
    return deepCopy(head)