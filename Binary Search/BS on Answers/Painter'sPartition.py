'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/painter-s-partition-problem_1089557

Problem Statement: Given an array/list of length ‘N’, where the array/list represents the boards and each element of the given array/list represents the length of each board. 
Some ‘K’ numbers of painters are available to paint these boards. 
Consider that each unit of a board takes 1 unit of time to paint. You are supposed to return the area of the minimum time to get this job done of painting all the ‘N’ boards under
the constraint that any painter will only paint the continuous sections of boards.

Example :
Input Format: N = 4, boards[] = {5, 5, 5, 5}, k = 2
Result: 10
Explanation: We can divide the boards into 2 equal-sized partitions, so each painter gets 10 units of the board and the total time taken is 10.

'''
# Brute Force 
def brute(arr,k):
    n = len(arr)
    
    mini = max(arr)
    maxi = sum(arr)
    
    for i in range (mini,maxi+1):
        if possi(arr,i)  == k :
            return i 
        
    return mini

# Helper Function 
def possi(arr,painter):
    n = len(arr)
    totalP = 0 
    people = 1 
    for i in range (n):
        if totalP + arr[i] <= painter :
            totalP += arr[i] 
        else:
            people += 1 
            totalP = arr[i] 
            
    return people
        
# Test Run 
# print(brute([10,20,30,40],2))

# Optimal Approach 
def optimal (arr,k):
    low = max(arr)
    high = sum(arr)
    
    while(low <= high):
        mid = (low + high)// 2
        
        maxi = summation(arr,mid)
        if maxi > k :
            low = mid + 1 
        else:
            high = mid -1 
    return low 


# Helper Function 
def summation(arr,paint):
    n = len(arr)
    totalP = 0 
    people =1 
    
    for i in range (n):
        if totalP + arr[i] <= paint :
            totalP += arr[i]
            
        else:
            people += 1 
            totalP = arr[i] 
    return people

        
# Test Run 
print(optimal([10,20,30,40],2))