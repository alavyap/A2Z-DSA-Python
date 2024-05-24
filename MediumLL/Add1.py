'''
GFG :> https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
Coding Ninja :> https://www.naukri.com/code360/problems/add-one-to-a-number-represented-as-linked-list_920557?leftPanelTabValue=PROBLEM
A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.
Example :
Input:
LinkedList: 4->5->6
Output: 457
Explanation: 4->5->6 represents 456 and when 1 is added it becomes 457. 
'''

# Brute Force 
def addingOne(head):
    
    # Edge Case 
    if not head :
        return Node(1)
    
    head = reversing(head)
    temp = head 
    carry = 1
    
    while temp : 
        temp.data = temp.data + carry 
        
        if temp.data < 10 :
            carry = 0 
            break
        
        else:
            temp.data = 0 
            carry = 1 
        temp = temp.next
        
    
    
    # If the carry is 1 
    if carry == 1 :
        new_node = Node(1)
        
        head = reversing(head)
        
        new_node.next = head 
        return new_node
        
    head = reversing(head)
    return head   
        
    
def reversing(head):
    if not head :
        return None 
    temp = head 
    prev = None 
    
    while temp:
        new_node = temp.next 
        temp.next = prev
        prev = temp
        temp = new_node
    return prev 

# Time : O(3N) and Space : O(1)


# Optimal Approach

def opAdd(head):
    carry = helper(head)
    if carry == 1 :
        new_node = Node(1)
        new_node.next = head 
        head = new_node
    return head 

# Helper Function
def helper(temp):
    if temp is None :
        return 1 
    carry = helper(temp.next)
    temp.data += carry 
    
    if temp.data < 10 :
        return 0 
    temp.data = 0 
    return 1 

# Time : O(N) & Space : O(N)