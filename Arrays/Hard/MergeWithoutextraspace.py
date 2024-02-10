'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/merge-two-sorted-arrays-without-extra-space_6898839?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode :> https://leetcode.com/problems/merge-sorted-array/description/

Problem statement: Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order. 
Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.

Example :
Input: 
n = 4, arr1[] = [1 4 8 10] 
m = 5, arr2[] = [2 3 9]
Output: 
arr1[] = [1 2 3 4]
arr2[] = [8 9 10]
Explanation: After merging the two non-decreasing arrays, we get, 1,2,3,4,8,9,10.
'''

# Brute Force 
def merge(arr1,arr2):
    '''
    n = len(arr1)
    m = len(arr2)
    for i in range (m):
        if arr1[n-1] > arr2[i] :
            arr1.append(arr2[i])
    arr1.sort()
    return arr1
    '''
    n = len(arr1)
    m = len(arr2)
    right = 0 
    left = 0 
    index = 0 
    ans = [0] * (n+m)
    
    while (left < n and right < m ):
        if arr1[left] <= arr2[right]:
            ans[index] = arr1[left]
            left += 1 
            index += 1 
        else :
            ans[index] = arr2[right] 
            right  += 1 
            index += 1
        
    # If right pointer reached the end 
    while (left <n):
        ans[index] = arr1[left]
        left += 1
        index += 1 
    
    # If left pointer reached the end 
    while (right <m) :
        ans[index] = arr2[right]
        right += 1 
        index += 1 
    
    # Inserting the remaing elements in the ans from the left out arrays
    for i in range (n+m):
        if i < n:
            arr1[i] = ans[i]
        else :
            arr2[i-n] = ans[i]
    return ans 
# Test Run 
# print (merge ([1,4,8,10],[2,3,9]))  
# print (merge ([1,8,8],[2,3,4,5])) 

# Optimal Approach > Two Pointers 
def mergeandSort(nums1,nums2):
    n= len(nums1)
    m = len(nums2)
    left = n-1
    right = 0 
    
    # Swap the elements until nums1 is smaller than nums2 
    while (left > 0 and right <m):
        if nums1[left] > nums2[right]:
            nums1[left],nums2[right] = nums2[right], nums1[left]
            left -= 1 
            right += 1 
            
        else :
            break 
        
    nums1.sort() 
    nums2.sort() 
    return nums1,nums2

# Test Run 
# print (mergeandSort([1,4,8,10],[2,3,9]))

# Optimal Approach :>> GAP Method (comes for shell sort)

# Helper Function 
def swapper(nums1,nums2,ind1,ind2):
    if nums1[ind1] > nums2[ind2]:
        nums1[ind1], nums2[ind2] = nums2[ind2], nums1[ind1]
        

# Main function 
def mergewithGap(nums1,nums2):
    n = len(nums1)
    m = len(nums2)
    
    total_len = n + m 
    gap = (total_len //2) + (total_len %2) 
    
    while gap > 0 :
        
        # Pointers 
        left = 0 
        right = left + gap 
        
        while right < total_len : 
            
            # Left in nums 1 && right in nums2 
            if  left < n and right >= n : 
                swapper(nums1,nums2,left, right -n)
                
            # Both  in nums2  
            elif left >= n:
                swapper (nums1, nums2, left - n, right - n)
            #  When both are in nums1 
            else :
                swapper(nums1,nums2, left,right)
            left += 1 
            right += 1 
            
        # If the gap is 1 
        if gap == 1 : 
            break  
        
        # Else 
        gap = (gap //2) + (gap %2)
    
                
    return nums1,nums2

# Test Run
print (mergewithGap([1,4,8,10],[2,3,9]))