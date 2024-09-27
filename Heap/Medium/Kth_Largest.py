'''

LeetCode :> https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''

# Using Heap DS
import heapq

def findK(nums,k):
    min_heap = [] 
    
    for i in nums :
        if len(min_heap) < k :
            heapq.heappush(min_heap,i)
        else :
            if i > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,i)
    return min_heap[0]

nums=  [3,2,3,1,2,4,5,5,6]
k = 4
print(findK(nums,k))




# Using Quick Sort Algorithm > Exceeds time limit 
import random

def findKth(nums,k):
    def quick(left,right,k):
        pivot = random.randint(left,right)
        pivot_value = nums[pivot]
        
        nums[pivot], nums[right] = nums[right], nums[pivot]
        
        
        store_index = left 
        for i in range (left,right):
            if nums[i] < pivot_value :
                nums[store_index],nums[i] = nums[i], nums[store_index]
                store_index += 1 
                
                
        nums[right], nums[store_index] = nums[store_index], nums[right]
        
        if k == right - store_index + 1 :
            return pivot_value
        elif k  < right - store_index + 1 :
            return quick(store_index + 1, right, k )
        else :
            return quick(left,store_index - 1 , k - (right - store_index + 1 ))
    return quick(0,len(nums) -1, k )




nums=  [3,2,3,1,2,4,5,5,6]
k = 4
print(findKth(nums,k))

