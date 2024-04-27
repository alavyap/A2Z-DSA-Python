'''
Coding Ninja :> https://www.naukri.com/code360/problems/count-with-k-different-characters_1214627
Problem statement
You are given a string 'str' of lowercase alphabets and an integer 'k' .

Your task is to return the count all the possible substrings that have exactly 'k' distinct characters.

For example:
'str' = abcad and 'k' = 2. 
We can see that the substrings {ab, bc, ca, ad} are the only substrings with 2 distinct characters. 
Therefore, the answer will be 4.    
'''

# Better Approach 
# T: O(N *2)
# S: O(N *3)
from collections import defaultdict
from tkinter import W

def countCharacter(s, k):
    ans = []
    res = ""
    for i in range(len(s)):
        res = ""
        for j in range(i, len(s)):
            if s[j] not in res:
                res += s[j]
            if len(res) == k:
                ans.append(res)
            elif len(res) > k:
                break
    # return len(ans)
    return ans


# Test Run 
# print(countCharacter("aacfssa",3))


# Optimal Code 
def countDis(s,k):
    ans = helper(s,k) - helper(s,k-1)
    
    return ans 

def helper(s,k):
    i = 0 
    j = 0 
    
    curCount = 0 
    result = 0 
    
    count = [0] *26 

    while j < len(s):
        index = ord(s[j]) -ord("a") 
        
        count[index] += 1 
        
        if count[index] ==1 :
            curCount += 1 
        
        while curCount > k :
            count[ord(s[i]) - ord("a")] -= 1 

            if count[ord(s[i]) - ord("a")] == 0 :
                curCount -= 1 
            i += 1
     
        result += (j -i +1)
        j += 1 
    return result
    
    
        
# Test Run 
print(countDis("aacfssa",3))