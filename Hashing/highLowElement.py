'''

Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

'''

def highLow (a):
    count = {}
    for i in range (len(a)):
        if a[i] not in count :
            count [a[i]] =1
        else:
            count [a[i]] +=1
            
    maX_key = max(count, key= count.get)
    miN_key = min(count,key = count.get)
            
            
    return f"{maX_key} {miN_key}"

# Test Run 
# print(highLow([10,5,10,15,10,5]))


# Coding Ninja
'''
You are given an array of size n. Find the highest and the lowest frequency elements.
If there are multiple elements that have the highest frequency or lowest frequency, pick the smallest element

'''

from multiprocessing.util import DEFAULT_LOGGING_FORMAT
from token import LEFTSHIFT
from turtle import right
from typing import List

def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    count = {}
    for i in range (len(v)):
        if v[i] in count:
            count[v[i]] += 1
        else:
            count[v[i]] = 1
            
    # for getting the max and min
    maXvalue = max(count.values())
    miNvalue = min(count.values())
                                                                                    # Time Complexity : O(n +k)
                                                                                    # Space Complexity: O(k)                                                                             
    maXkey = [k for k,v in count.items() if v == maXvalue]
    miNkey = [k for k,v in count.items() if v == miNvalue]
        
    maxElement = min(maXkey)
    minElement = min(miNkey)
    return maxElement ,minElement

# Test Run
# print(getFrequencies([10,10,10,3,3,3]))


'''
LeetCode : Problem 1838  Frequency of the Most Frequent Element

'''
    # this apporach works fine with 2 testcases but is fails for the nums= [1,4,8,13] and k = 5 : the output should be 2 but it is giving 4 
'''
def maxFrequency( nums: List[int], k: int) -> int:
    count = {k for k in range (1,k+1)}
    maxKey = 0
    pos = 1
    
    # this is doing the same task as max does 
    for i in range (len(nums)):
        if nums[i] > maxKey:
            maxKey = nums[i] 
        
        if (maxKey - nums[i-1]) in count :
            pos += 1
        else:
            pos = 1  

    return pos
print(maxFrequency([1,2,4],5))
    
'''
# you need to be familar with sliding window method for solving this problem 
# here is the link for the same : https://youtu.be/MK-NZ4hN7rs
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        leftSide = maxValue = sum = 0
        
        for rightSide in range (len(nums)):
            sum += nums[rightSide]
            
            while (rightSide - leftSide + 1) * nums[rightSide] - sum > k :
                sum -= nums[leftSide]
                leftSide += 1                                               
                                                                                    #Time Complexity : O(n log n)
                                                                                    #Space Complexity : O(1)
                
            maxValue = max(maxValue, rightSide - leftSide +1)
        return maxValue
        
# Example usage:
solution = Solution()
print(solution.maxFrequency([1, 2, 4], 5))  # Output: 3
print(solution.maxFrequency([3, 9, 6], 2))  # Output: 1
print(solution.maxFrequency([1, 4, 8, 13], 5))  # Output: 2


