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
    
    temp_1 = head 
    res = [] 
    
    while temp_1 is not None :
        temp_2 = temp_1.next 
        
        while (temp_2 is not None and temp_1.data + temp_2.data <= target ):
            if (temp_1.data + temp_2.data == target) :
                res.append((temp_1.data,temp_2.data))
                
            temp_2 = temp_2.next
    temp_1 = temp_1.next 
    
    return res

# Time: O(N*2) ; Space: O(1)



# Optimal Approach 

def pairs_finder(head,target):
    
    left = head 
    right = find_tail(head)  #T:O(N)
    result = []
    
    while left.data < right.data :
        if left.data + right.data == target :
            result.append((left.data,right.data))
            left = left.next
            right = right.prev
        elif (left.data + right.data >target ):
            right = right.prev 
        else: 
            left = left.next 
            
       
    return result
    
# Time :O(N) & Space: O(1) 
    
# Tail Finder 
def find_tail(head):
    
    temp = head 
    while temp.next is not None:
        temp = temp.next 
    return temp