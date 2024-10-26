'''
Coding Ninja :  https://www.naukri.com/code360/problems/reverse-words-in-a-string_696444
Leetcode : https://leetcode.com/problems/reverse-words-in-a-string/description/
Problem Statement: Given a string s, reverse the words of the string.
Example :
Input: s=”this is an amazing program”
Output: “program amazing an is this”
'''

def reverserWords(str):
    res = ''
    i = 0 
    n = len(str)
    
    while (i <n ):
        while i <n and str[i] == " ":
            i += 1 
        if i >=n :
            break 
        j  = i + 1 
        
        while j <n and str[j] != " ":
            j += 1 
        word = str[i:j]
        
        if len(res) == 0 :
            res = word 
            
        else :
            res = word + " " + res
            
        i = j + 1 
    return res         

# Test Run 
print(reverserWords("  hello world  "))