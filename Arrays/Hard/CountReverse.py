'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/team-contest_6840309?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode :> https://leetcode.com/problems/reverse-pairs/description/

Problem Statement: Given an array of numbers, you need to return the count of reverse pairs. 
Reverse Pairs are those pairs where i<j and arr[i]>2*arr[j].

Example :
Input: N = 5, array[] = {1,3,2,3,1)
Output: 2 
Explanation: The pairs are (3, 1) and (3, 1) as from both the pairs the condition arr[i] > 2*arr[j] is satisfied.

'''
# Brute Force 

def bf (arr):
    n = len(arr)
    count = 0 
    for i in range (n):
        for j in range (i+1,n):          
            if arr[i] > 2 *arr[j]  :
                count += 1 
                
    return count 

# Test Run 
# print(bf ([1,3,2,3,1]))

# In this question you have to mention that you are distorting  the array , inCase you have any problem i can take a copy of your array and solve it 


# Optimal Approach 
def op (arr): 
    n = len(arr)
    return helper(arr,0,n-1)


def helper(arr,low,high):
    count = 0 
    if low >= high:
        return count 
    
    mid = (low + high) //2
    count += helper(arr,low,mid)
    count += helper (arr,mid+1,high)
    count += countPairs(arr,low,mid,high)
    merge(arr,low,mid,high)
    return count 



def countPairs(arr,low,mid,high):
    right = mid+1 
    count = 0 
    for i in range (low,mid+1):
        while right <=high and arr[i] > 2 * arr[right] : 
            right += 1 
        count += (right - (mid+1))
    return count

    

def merge (arr,low,mid,high):
    
    temp = []       #Temporary Array
    left = low      #starting index of the left half of the array 
    right = mid + 1     #starting index of the right half of the array
    
    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high :
        if arr[left] <= arr[right] :
            temp.append(arr[left])
            left += 1 
        else :
            temp.append(arr[right])
            right += 1 
            
    # if elements on the left half are still left
    while left <= mid :
        temp.append(arr[left])
        left += 1 
     
    # if elements on the right half are still left   
    while right <= high :
        temp.append(arr[right])
        right += 1 
        
    # transferring all elements from temporary to arr
    for i in range (low,high+1):
        arr[i] = temp[i-low]
    




# Helper Function 

# Test Run 
print(op ([1,3,2,3,1]))