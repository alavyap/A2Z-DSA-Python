'''
Given a string, check if the string is palindrome or not.  
A string is said to be palindrome if the reverse of the string is the same as the string.

'''

def isAPalindrome(string):
    string = string.lower().replace(" ", "")
    if len(string) <=1:
        return False
    n1 = string[::-1].lower().replace(" ","")
    if (string ==n1):
        return True
    else:
        return False
    
    
    
# Test Run
# print(isAPalindrome('raceCar  '))



'''
LeetCode question is also same, just change of words 
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
'''

def isPalindrome( s: str) -> bool:
    newS = ''
    for char in s:
        if char.isalnum():
            newS += char.lower()
    return newS == newS[::-1]


# Test Run
print(isPalindrome('race:car'))


# I would prefer to user the leetcode one as it is using all the things that is taught as a beginner. 
