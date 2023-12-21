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
def maxFrequency( nums: List[int], k: int) -> int:
    count = {}
    for i in range (len(nums)):
        if nums[i] in count:
            count[nums[i]] += 1 
        else:
            count[nums[i]] = 1
    
        '''
        UNSOLVED
        '''
    
  
    return count

print(maxFrequency([1,2,4],5))