'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/capacity-to-ship-packages-within-d-days_1229379
LeetCode :> https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

Problem Statement: You are the owner of a Shipment company. You use conveyor belts to ship packages from one port to another. The packages must be shipped within ‘d’ days.
The weights of the packages are given in an array ‘of weights’. The packages are loaded on the conveyor belts every day in the same order as they appear in the array. 
The loaded weights must not exceed the maximum weight capacity of the ship.
Find out the least-weight capacity so that you can ship all the packages within ‘d’ days.

Example 1:
Input Format: N = 5, weights[] = {5,4,5,2,3,4,5,6}, d = 5
Result: 9
Explanation: If the ship capacity is 9, the shipment will be done in the following manner:
Day         Weights            Total
1        -       5, 4          -        9
2        -       5, 2          -        7
3        -       3, 4          -        7
4        -       5              -        5
5        -       6              -        6
So, the least capacity should be 9.

Example 2:

Input Format: N = 10, weights[] = {1,2,3,4,5,6,7,8,9,10}, d = 1
Result: 55
Explanation: We have to ship all the goods in a single day. So, the weight capacity should be the summation of all the weights i.e. 55.
'''

# Brute Force 
def brute (arr,days):
    
    # Values 
    maxi = max(arr)
    tSum = sum(arr)
        
    for i in range (maxi,tSum +1):
        if findCap(arr,i)  <= days:
            return i 

    # Dummy 
    return -1
        
        
# Helper Function 
def findCap(arr,cap):
    n = len(arr)
    load = 0 
    days = 1 
    
    for i in range (n):
        if load + arr[i]  > cap :
            days += 1 
            load = arr[i] 
        else :
            load += arr[i] 
    return days 

    
# Test Run 
# print(brute([5,4,5,2,3,4,5,6],5))



# Optimal Approach 

def optimal (weights,d):
    low = max(weights)
    high = sum(weights)
    
    while (low <= high):
        mid = (low + high) //2 
        
        if findDays(weights,mid) <= d :
            high = mid -1 
        else :
            low = mid + 1 
            
    return low 


# Helper Function 
def findDays(weights,cap):
    n = len(weights)
    load = 0 
    days = 1 
    for i in range (n):
        if load + weights[i] > cap :
            days += 1 
            load = weights[i] 
            
        else :
            load += weights[i] 
            
    return days

# Test Run 
print(optimal([5,4,5,2,3,4,5,6],5))