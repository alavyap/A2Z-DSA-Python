'''
Coding Ninja :> https://www.naukri.com/code360/problems/reverse-words_7037425
LeetCode: > https://leetcode.com/problems/reverse-words-in-a-string/description/
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example :
Input: s = "the sky is blue"
Output: "blue is sky the"

'''
def reverseWords(s):
    ans = ""
    i = 0 
    
    while (i <len(s)):
        while i < len(s) and s[i] == " " :
            i+= 1 
        if i >= len(s):
            break
        j = i + 1 
        
        while (j < len(s)) and s[j] != " ":
            j += 1 
            
        word = s[i:j]
        
        if len(ans) == 0 :
            ans = word 
        else:
            ans = word + " " + ans 
        i = j+ 1
    return ans

# Test Run 
print(reverseWords("the sky is blue"))