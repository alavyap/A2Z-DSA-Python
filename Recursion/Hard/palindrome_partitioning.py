'''

LeetCode :> https://leetcode.com/problems/palindrome-partitioning/description/


Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.

'''

def partition(s):
    
    res = [] 
    path = [] 
    
    def partion_helper(index):
        if index == len(s):
            res.append(path[:])
            return 
        
        for i in range (index,len(s)):
            if isPalindrome(s,index,i):
                path.append(s[index : i + 1])
                partion_helper(i+1)
                path.pop()
                
    
    def isPalindrome(s,start,end):
        while start <= end :
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1 
        return True
    partion_helper(0)
    return res
            