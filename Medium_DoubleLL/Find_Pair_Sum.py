'''
GFG :> https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1
Coding Ninjas :> https://www.naukri.com/code360/problems/find-pairs-with-given-sum-in-doubly-linked-list_1164172

Problem Statement: Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target.
Example :
Input:  
1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
target = 7
Output: (1, 6), (2,5)
Explanation: We can see that there are two pairs 
(1, 6) and (2,5) with sum 7.

'''

# Brute Force 
def find_Pairs(head,target): 
    
    slow = head 
    fast = head 
    count = 0 
    while slow is not None :
        
        if slow.data + fast.data == target :
            
            count += 1 
            slow = slow.next 
            fast = slow 
        fast = fast.next 
    return count