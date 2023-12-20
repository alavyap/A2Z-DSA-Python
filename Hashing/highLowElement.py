'''

Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

'''

def highLow (a):
    count = {}
    for i in range (len(a)):
        if a[i] not in count :
            count [a[i]] =1
        else:
            count [a[i]] +=1
            
    maX_key = max(count, key= count.get)
    miN_key = min(count,key = count.get)
            
            
    return f"{maX_key} {miN_key}"

# Test Run 
# print(highLow([10,5,10,15,10,5]))


# Coding Ninja
'''
You are given an array of size n. Find the highest and the lowest frequency elements.
If there are multiple elements that have the highest frequency or lowest frequency, pick the smallest element

'''

from typing import List

def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    count = {}
    for i in range (len(v)):
        if v[i] not in count :
            count [v[i]] =1
        else:
            count [v[i]] +=1
    maX_key = max(count, key= count.get)
    miN_key = min(count,key = count.get)
    
    # using result because the site was giving error for using f string so had to add the max and min in a array and then output it.
    result = []
    if maX_key != miN_key :
        result.append(maX_key)
        result.append(miN_key)
    else:
      result.append(miN_key)
      result.append(miN_key)
    return result
# UNSOLVED
print(getFrequencies([10,10,10,3,3,3]))