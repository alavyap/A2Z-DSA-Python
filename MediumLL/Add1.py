'''
GFG :> https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
Coding Ninja :> https://www.naukri.com/code360/problems/add-one-to-linked-list_920456?interviewProblemRedirection=true&search=Add%201%20&leftPanelTabValue=PROBLEM
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
    if head is None :
        return Node(1)
    
    carry = 1 
    temp = head 
    prev = None 
    
    while temp :
        next_node = temp.next 
        temp.next = prev 
        prev = temp 
        temp = next_node 
        
    # Add 1 to first node 
    temp.data += carry 
        
    while carry and temp.next :
        temp = temp.next 
        temp.data += carry 
        carry = temp.data // 10  #Update the carry for the next node 
            
    if carry:
        new_head = Node(carry)
        new_head.next  = head 
        head = new_head
           
    return head 