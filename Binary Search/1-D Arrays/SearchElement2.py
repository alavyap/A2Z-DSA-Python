'''
Coding Ninja :>  https://www.codingninjas.com/studio/problems/search-in-a-rotated-sorted-array-ii_7449547
LeetCode :> https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. 
Now the array is rotated at some pivot point unknown to you. 
Return True if k is present and otherwise, return False. 

Example :
Input Format: arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
Result: True
Explanation: The element 3 is present in the array. So, the answer is True.

'''

# Brute Force 
def brute (arr,k):
    n = len(arr)
    for i in range (n):
        if arr[i] == k :
            return True 
    return False


# Test Run 
# print(brute([7, 8, 1, 2, 3, 3, 3, 4, 5, 6],3))


# Optimal Approach 

def optimal (arr,key):
    
    n = len(arr)
    low = 0 
    high = n- 1 
    
    while (low <= high):
        mid = (low + high) // 2
        if arr[mid] == key :
            return True 
        
        #  Edge Case 
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1 
            continue
        # If the key is in left part of the sorted array
        if arr[low] <= arr[mid]:   
            if arr[low] <= key and key <= arr[mid]:
                high = mid - 1 
            else :
                low = mid + 1 
                
        else :
            # If the key is in the right part of the sorted array
            if arr[mid] <= key and key <= arr[high]:
                low = mid + 1 
            else :
                high = mid - 1 
    return False

# Test Run 
print(optimal([7, 8, 1, 2, 3, 3, 3, 4, 5, 6],3))
# Not Fully Submited on Coding Ninja 