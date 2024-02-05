'''
Coding Ninja : >
LeetCode : >
                                    ***** PRE- REQUISITE >> MAJORITY ELEMENT (N/2) TIMES*****
Problem Statement: Given an array of N integers. Find the elements that appear more than N/3 times in the array. If no such element exists, return an empty vector.
Example :
Input Format: N = 5, array[] = {1,2,2,3,2}
Result: 2
Explanation: Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.
'''

# Brute Force  > Using a dictionary 
def majority(n,arr):
    req = n//3
    dict = {}
    ans = []
    #  Storing the values in a dictionary 
    for i in range (n):
        if arr[i] in dict :
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1 
    for key,value in dict.items():
        if value > req: 
            ans.append(key)
    return ans
        
# Test Run 

# print(majority(6,[11,22,11,22,22,11]))
print(majority(5,[1,2,2,3,2]))