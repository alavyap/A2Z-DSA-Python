'''
GFG :> https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1
Coding Ninja :> https://www.naukri.com/code360/problems/remove-duplicates-from-a-sorted-doubly-linked-list_2420283

Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.
Example :
Input:
n = 6
1<->1<->1<->2<->3<->4
Output:
1<->2<->3<->4
Explanation:
Only the first occurance of node with value 1 is 
retained, rest nodes with value = 1 are deleted.

'''
# Optimal Approach
def remove_Duplicates(head):   
    
    temp = head 
    
    while temp is not None and temp.next is not None : 
        if temp.data == temp.next.data : 
            next_node = temp.next.next 
            temp.next = next_node
            if next_node is not None :
                next_node.prev = temp
        else :
            temp = temp.next 
    return head 



