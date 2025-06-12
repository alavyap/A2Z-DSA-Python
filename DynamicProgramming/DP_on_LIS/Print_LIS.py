'''
Print the Longest Increasing Subsequence
'''


def printLIS(nums):
    
    n = len(nums)
    dp = [1] * n 
    hashMap = [i for i in range (n)]
    
    for i in range (n): 
        for prevInd in range (i): 
            if nums[prevInd] < nums[i] and dp[prevInd] +1 > dp[i]: 
                dp[i] = dp[prevInd] +1 
                hashMap[i] = prevInd
                
    maxLen = max(dp)
    lastInd  = dp.index(maxLen)
    
    list = [nums[lastInd]]
    while hashMap[lastInd] != lastInd : 
        lastInd = hashMap[lastInd]
        list.append(nums[lastInd])
        
    list.reverse() 
    return list