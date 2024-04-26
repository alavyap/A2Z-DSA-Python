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
print(countCharacter("aacfssa",3))