'''

LeetCode :> https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105



'''


# Brute Force 
def trap(height): 
    n = len(height)
    trapped = 0 
    
    for i in range (n):
        j = i 
        leftMax = 0 
        rightMax = 0 
        while j >= 0 :
            leftMax = max(leftMax,height[j])
            j -= 1 
        j = i 
        while j < n :
            rightMax = max(rightMax,height[j]) 
            j +=  1 
            
        trapped += min(leftMax,rightMax) - height[i]
        
    return trapped
    
    


# Better Approach

def trapWater(height):
    
    n = len(height)
    prefix = [0] * n
    suffix = [0] * n 
    trappedWater = 0 
    
    prefix[0] = height[0]
    suffix[n-1] = height[n-1]
    
    for i in range (1,n):
        prefix[i] = max(prefix[i-1], height[i])
    
    for i in range (n -2, -1, -1):
        suffix[i] = max(suffix[i + 1], height[i])
        
    for i in range (n):
        trappedWater += min(prefix[i],suffix[i])- height[i]
    return trappedWater


# Optimal Approach
def waterTrap(height):
    n = len(height)
    left = 0 
    right = n-1 
    maxLeft = 0
    maxRight = 0 
    ans = 0
    
    while left <= right :
        if height[left] <= height[right]:
            if height[left] >= maxLeft :
                maxLeft = height[left]
            else :
                ans += maxLeft - height[left]
            left += 1 
            
        else :
            if height[right] >= maxRight :
                maxRight = height[right]
            else:
                ans += maxRight - height[right]
            right -= 1 
    return ans

# a = [4,2,0,3,2,5]
a = [0,1,0,2,1,0,1,3,2,1,2,1]
print(waterTrap(a))