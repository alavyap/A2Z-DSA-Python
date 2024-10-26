'''
Coding Ninja :> https://www.naukri.com/code360/problems/sorting-characters-by-frequency_1263699
LeetCode :> https://leetcode.com/problems/sort-characters-by-frequency/description/
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example :
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

'''

from collections import Counter, defaultdict


# Brute Force 
def frequencySort(s):
    s_sorted =''.join(sorted(s))
    return s_sorted

# Test Run 
# print(frequencySort('tree'))

# Better Approach 
def sortFrequency(s):
    count = Counter(s)   # this is doing the hashing for us instead of iterating all over
    
    buckets = defaultdict(list) # list -> [char]
    
    
    for char,cnt in count.items():
        buckets[cnt].append(char)
        
        
    res = []
    
    for i in range (len(s),0,-1):
        for c in buckets[i] :
            res.append(c*i)
            
    return ''.join(res)
   
   

# Test Run 
# print(sortFrequency('tree'))

