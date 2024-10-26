'''
LeetCode :> https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

'''

import heapq
from unittest import result
def KthMerge(lists):
    k = len(lists)
    min_heap = [] 
    result = []
    
    
    for i in range (k):
        if lists[i] :
            heapq.heappush(min_heap,(lists[i][0],i,0))
            
    while min_heap :
        val,list_idx,element_idx = heapq.heappop(min_heap)
        
        result.append(val)
        
        
        if element_idx + 1 < len(lists[list_idx]) :
            next_element = lists[list_idx][element_idx +1 ]
            heapq.heappush(min_heap,(next_element,list_idx,element_idx+1))
    return result 


# Test
list = [[1,4,5],[1,3,4],[2,6]]
print(KthMerge(list))

# LeetCode Solution 

def MergeK (lists):
    ListNode.__lt__ = lambda self,other: self.val < other.val #type:ignore
    
    min_heap = [] 
    dummy = ListNode(0) #type:ignore
    current = dummy
    
    
    # Push the head of each non_empty list into the heap 
    for i,l in enumerate(lists) :
        if l :
            heapq.heappush(min_heap,(l.val,i,l))
            
    while min_heap : 
        val,i,node = heapq.heappop(min_heap)
        
        current.next = node 
        current = current.next 
        
        
        if node.next :
            heapq.heappush(min_heap,(node.next.val,i,node.next))
            
    return dummy.next