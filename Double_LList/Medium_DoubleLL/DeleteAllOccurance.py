'''
GFG :>   https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1
Coding Ninjas :> https://www.naukri.com/code360/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list_8160461

Problem Statement : You are given the head_ref of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key if it is present and return the new DLL.
Example :
Input: 
2<->2<->10<->8<->4<->2<->5<->2
2
Output: 
10<->8<->4<->5
Explanation: 
All Occurences of 2 have been deleted.
'''

# Brute Force 
def remove_dupli(head,k):
    while head and head.data==k  :
        head = head.next
    
    temp = head 
    while temp is not None:    
        if temp.data == k :
           new_next = temp.next 
           new_prev = temp.prev 
            
           new_prev.next = new_next 
           temp = new_next
        else :
            temp = temp.next
                 
    return head

# The above code misses the test case of If the last node is k then there will be only previous not next  and vice versa for the head or the first node 

# Optimal Code 

def delete_All_Occurence(head,k):
    temp = head 
    
    while temp is not None :
        if temp.data == k :
            if temp == head  :
                head = temp.next 
                
            next_node = temp.next 
            prev_node = temp.prev 
            
            if next_node is not None :
                next_node.prev = prev_node 
            if prev_node is not  None :                             #Time Complexity :> O(N)
                prev_node.next = next_node                          #Space Complexity :> O(1)
                
            temp = next_node 
        else :
            temp = temp.next
    return head 


