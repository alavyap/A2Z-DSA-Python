'''
Coding Ninja >> https://www.codingninjas.com/studio/problems/superior-elements_6783446?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

Problem Statement: Given an array, print all the elements which are leaders. 
A Leader is an element that is greater than all of the elements on its right side in the array. [element, >>>]
Example:
Input:
arr = [10, 22, 12, 3, 0, 6]
Output:
22 12 6
Explanation:
6 is a leader. In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.
'''
# Brute Force 
def leader_bf (arr):
    n = len(arr)
    a = []
    for i in range (n-1):
       if arr[i] > arr[i+1] and arr[i] > arr[i +2]:
           a.append(arr[i])
    a.append(arr[n-1])
    return a
   

# Optimal Approach 
def leader (a):
    n = len(a)   
    if n == 0 :
        return 
    max_right = a[n-1]
    leaders = [a[n-1]]

    for i in range (n-2,-1,-1):                             #Time Complexity  > O(N)
        if a[i] > max_right :                               #Space Complexity > O(N)
            leaders.append(a[i])
            max_right = a[i]
    leaders.reverse()
    return leaders
            
# Test Run 
print (leader ([10, 22, 12, 3, 0, 6]))