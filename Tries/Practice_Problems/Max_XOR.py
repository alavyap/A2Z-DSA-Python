'''
Link :> https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 231 - 1

'''
class TrieNode: 
    def __init__(self):
        self.children = [None,None]
        
class Trie: 
    def  __init__(self):
        self.root = TrieNode() 
        
    def insert(self,num):
        node = self.root
        for i in range(31,-1,-1):
            bit = (num >> i) & 1 
            if node.children[bit] is None:
                node.children[bit] = TrieNode() 
            node = node.children[bit]
            
    def max_XOR(self,num):
        node = self.root
        max_xor  = 0 
        
        for i in range (31,-1,-1): 
            bit = (num >>i ) & 1 
            opposite_bit = 1 - bit 
            if node.children[opposite_bit]: 
                max_xor |= (1 << i)
                node = node.children[opposite_bit]
            else:
                node = node.children[bit]
        return max_xor
    
def findMax(nums):
    trie = Trie()
    max_result  = 0 
    
    for num in nums:
        trie.insert(num)
        
    for num in nums:
        max_result = max(max_result,trie.max_XOR(num))
    return max_result

