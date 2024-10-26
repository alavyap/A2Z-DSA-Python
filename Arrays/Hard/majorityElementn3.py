'''
Coding Ninja : > https://www.codingninjas.com/studio/problems/majority-element_6915220?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode : > https://leetcode.com/problems/majority-element-ii/
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
# print(majority(5,[1,2,2,3,2]))

# Optimal Approach >> Moore's Voting Algorithm
def majorityElementN3(v):
    n = len(v)
    
    # Initial Elements
    count1,count2 = 0,0 
    element1,element2 = float('-inf'), float('-inf')
    
    # Applying the extended version of Moore's Voting Algorithm
    for i in range (n):
        if count1 == 0 and element2 != v[i] :
            count1 = 1 
            element1 = v[i] 
        elif count2 == 0 and element1 != v[i] :
            count2 = 1
            element2 = v[i] 
            
        elif v[i] == element1 :
            count1 += 1 
        elif v[i] == element2 :
            count2 += 1 
            
        else :
            count1 -=1 
            count2 -= 1 
            
    # to store the output 
    ans = []
    # Manually Check the majority of the element 
    cnt1,cnt2 = 0,0 
    for i in range (n):
        if v[i] == element1 :
            cnt1 += 1 
        if v[i] == element2:
            cnt2 += 1 
    
    # Giving the minimum to check if the count is greater then the mini 
    mini = n//3 +1 
    if cnt1 >= mini :
        ans.append(element1)
    if cnt2 >= mini:
        ans.append(element2)
    return ans
    
# Test Run 
print( majorityElementN3([11,22,11,22,22,11]))