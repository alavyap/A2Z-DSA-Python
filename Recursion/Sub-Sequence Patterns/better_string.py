'''
GFG :> https://www.geeksforgeeks.org/problems/better-string/1

Given a pair of strings of equal lengths, Geek wants to find the better string. The better string is the string having more number of distinct subsequences.
If both the strings have equal count of distinct subsequence then return str1.

Example 1:

Input:
str1 = "gfg", str2 = "ggg"
Output: "gfg"
Explanation: "gfg" have 6 distinct subsequences whereas "ggg" have 3 distinct subsequences. 

Your Task:
You don't need to read input or print anything. Your task is to complete the function betterString() which takes str1 and str2 as input parameters and returns the better string.
Expected Time Complexity: O( N ), where N is the length of both provided strings.
Expected Auxiliary Space: O( N )

'''


# Brute Force 
def if_better (s1,s2):
    c1 = {}
    c2 = {} 
    
    def count_letter (s,count_dict):
        for char in s :
            if char in count_dict :
                count_dict[char] += 1
            else :
                count_dict[char] = 1 
                
    count_letter(s1,c1)
    count_letter(s2,c2)
    
    
    for keys in c1 :
        for keys in c2 :
            if c1[keys] == c2[keys] :
                return s1 
        
    