'''
LeetCode :> https://leetcode.com/problems/reverse-nodes-in-k-group/description/
Coding Ninja :> https://www.naukri.com/code360/problems/reverse-list-in-k-groups_983644

Problem Statement : Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
Example :
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

For example, if the linked list is 1->2->3->4->5, and 'k' is 3, we have to reverse the first three elements, and leave the last two elements unchanged. Thus, the final linked list being 3->2->1->4->5.


Follow-up: Can you solve the problem in O(1) extra memory space?
'''

# Brute Force 
def reverse_Group_K(head,k):
    # Time Complexity >> O(2N) and Space Complexity > O(1)
    temp = head 
    prev_last = None 
    
    while temp is not None :
        kth_node = getKthNode(temp,k)
        
        if kth_node is None :
            if prev_last :
                prev_last.next = temp 
            break 
        
        next_node =  kth_node.next 
        kth_node.next = None
        
        reverse_LinkedList(temp)
        
        
        if temp == head :
            head = kth_node 
        else :
            prev_last.next = kth_node 
            
        prev_last = temp 
        temp = next_node
        
    return head 

def getKthNode(temp,k):
    k -= 1 
    
    while temp is not None and k > 0 : 
        k -= 1 
        temp = temp.next 
    return temp 


def reverse_LinkedList(head):
    temp = head 
    prev = None 
    
    while temp is not None :
        front = temp.next 
        temp.next = prev 
        prev = temp 
        temp = front
    return prev
            
            
# Optimal Approach 
def reverseKthGroup(head,k):
    count = 0 
    temp = head 
    
    while temp :
        temp = temp.next 
        count += 1 
        
    n = count // k  
    # To find the total number of groups to rotate 
    
    prev = dummy = ListNode()
    dummy.next = head 
    while n :
        curr = prev.next 
        next_node = curr.next 
        for i in range (1,k):
            curr.next = next_node.next
            next_node.next = prev.next 
            prev.next = next_node
            next_node = curr.next 
        prev = curr 
        n -= 1 
    return dummy.next
        