'''
Link: https://www.codingninjas.com/studio/problems/traffic_6682625?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.
Example :
Input: prices = {1, 1, 0, 1, 1, 1}
Output: 3
Explanation: There are two consecutive 1's and three consecutive 1's in the array out of which maximum is 3.

'''

#  >> For striver question And LeetCode
def countMax(arr):
    maxCount = 0 
    currentCount = 0
    
    n = len(arr)
     
    for i in range (n):
        if arr[i] == 1 :
            currentCount += 1 
            if maxCount < currentCount :
                maxCount = currentCount 
       
        else:
            currentCount  = 0
    return maxCount

# Test Run
print(countMax([1,0,1,1,0,1]))

# Coding Ninja > GIven there are m 1's that are changed on 0 find the total number of consecutive 1's

def countOne(n,m,arr):
    ans=0
    count=0
    right = 0
    for left in range (n):
        while right < n and count <= m :
            if arr[right] == 0 :
                count += 1
                if count > m:
                    count -= 1 
                    break 
            right += 1
        if ans < (right - left):
            ans = (right-left)
        if arr[left] == 0:
            count -= 1
    return ans    
                
        
# Test Run 
# print (countOne(6,3,[0,1,0,0,1,0])) 



# def traffic(n: int, m: int, vehicle: [int]) -> int:
#     # Write your code here.
#     maxCount = 0 
#     currentCount = 0
#     flipsLeft = m

#     for i in range (n):
#         if vehicle[i] == 1:
#             currentCount += 1
#         elif flipsLeft > 0 :
#             currentCount += 1
#             flipsLeft -= 1 

#         else :
#             currentCount = 0


#         if maxCount < currentCount :
#             maxCount = currentCount 

#     return  maxCount