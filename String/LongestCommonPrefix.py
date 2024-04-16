'''
Coding Ninja:> https://www.naukri.com/code360/problems/longest-common-prefix_628874
LeetCode :> https://leetcode.com/problems/longest-common-prefix/description/
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example :
Input: strs = ["flower","flow","flight"]
Output: "fl"
Explanation: "fl is only  common prefix among the input strings.
'''

# Better Approach 
def longestPrefix(str):
    prefix = ""
    
    for i in str:
        if (len(i) < len(prefix) or prefix== " "):
            prefix = i 
            
            
    need = len(str)
    count = 0 
    res = ""
    while( need != count):
        count = 0 
        for i in str :
            if (prefix == i[:len(prefix)]):
                count += 1 
        res = prefix
        prefix = prefix[:-1]
    # Coding Ninja Solution
    if prefix == "":
        return "-1"
    if (need == count ):
        return res
    else:
        return ""
    
    
# Test Run 
# print(longestPrefix('“abcd”, “abc”, “abref”, “abcde”'))


# Optimal Approach 
def longestPrefix(strs):
    res = ""
    for i in range (len(strs[0])):
        for s in strs :
            if i == len(s) or s[i] != strs[0][i] :
                return res  
        res += strs[0][i]
        
    return res

# Test Run 

print(longestPrefix('“abcd”, “abc”, “abref”, “abcde”'))
