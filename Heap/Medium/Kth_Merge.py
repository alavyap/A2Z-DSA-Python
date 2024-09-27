'''
GFG :> https://www.geeksforgeeks.org/problems/merge-k-sorted-arrays/1

Given k sorted arrays arranged in the form of a matrix of size k * k. The task is to merge them into one sorted array. Return the merged sorted array ( as a pointer to the merged sorted arrays in cpp, as an ArrayList in java, and list in python).


Examples :
Input: k = 3, arr[][] = {{1,2,3},{4,5,6},{7,8,9}}
Output: 1 2 3 4 5 6 7 8 9
Explanation: Above test case has 3 sorted arrays of size 3, 3, 3 arr[][] = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]. The merged list will be [1, 2, 3, 4, 5, 6, 7, 8, 9].

Input: k = 4, arr[][]={{1,2,3,4},{2,2,3,4},{5,5,6,6},{7,8,9,9}}
Output: 1 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9 
Explanation: Above test case has 4 sorted arrays of size 4, 4, 4, 4 arr[][] = [[1, 2, 2, 2], [3, 3, 4, 4], [5, 5, 6, 6], [7, 8, 9, 9 ]]. The merged list will be [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9].

Expected Time Complexity: O(k2*Log(k))
Expected Auxiliary Space: O(k2)

Constraints:
1 <= k <= 100


'''

import heapq 

def KthArr(arr,k): 
    min_heap = [] 
    res = [] 
    
    for i in range (k):
        if arr[i] :
            heapq.heappush(min_heap,(arr[i][0],i,0))
            
            
    while min_heap :
        val,array_ind, element_ind = heapq.heappop(min_heap)
        res.append(val)
        
        
        if element_ind + 1 < len(arr[array_ind]):
            next_element = arr[array_ind][element_ind +  1]
            heapq.heappush(min_heap, (next_element,array_ind,element_ind +1))
    return res


# Test 
k1 = 3
arr1 = [[1,2,3],[4,5,6],[7,8,9]]
print(KthArr(arr1, k1))
        