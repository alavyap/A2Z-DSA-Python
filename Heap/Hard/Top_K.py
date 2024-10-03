'''
LeetCode :> https://leetcode.com/problems/top-k-frequent-elements/description/


Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


'''
from collections import Counter
def Ktop(nums,k):
    
    count = Counter(nums)
        
    # Sort the numbers based on their frequency in descending order
    sorted_nums = sorted(count, key=count.get, reverse=True)
        
    # Return the k most frequent elements
    return sorted_nums[:k]
    
    
    
def  TopK(nums,k):
    count = Counter(nums)
    
    buckets = [[] for _ in range (len(nums) +1 )]
    
    for num , freq in count.items() :
        buckets[freq].append(num)
        
    
    result = []
    
    for i in range (len(buckets) -1,0, -1): 
        result.extend(buckets[i])
        if len(result) >= k :
            
            return result[:k]
    
    return result
            