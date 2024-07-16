''' 
LeetCode :>  https://leetcode.com/problems/linked-list-cycle-ii/description/
Coding Ninja :> https://www.naukri.com/code360/problems/detect-the-first-node-of-the-loop_1112628?count=25&page=4&search=Linked%20List&sort_entity=order&sort_order=ASC&leftPanelTabValue=PROBLEM&customSource=studio_nav
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

Example :
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

'''
# Brute Force 

def brutecycle(head):

    # Edge Case 
    if head is None or head.next is None :
        return None 
    
    temp = head 
    dicti = set()
    
    while temp != None :
        if temp  in dicti :
            return temp 
        dicti.add(temp)
        temp = temp.next 
    return None

# Optimal Approach 
def detectCycle (head):
    
    # Edge Case 
    if head is None or head.next is None :
        return None 
    
    hare = head 
    tor = head
    
    while tor and hare and hare.next :
        tor = tor.next 
        hare = hare.next.next 
        
        
        if hare == tor :
            tor = head 
            
            while tor != hare :
                hare = hare.next 
                tor = tor.next 
            return tor
         
    return None