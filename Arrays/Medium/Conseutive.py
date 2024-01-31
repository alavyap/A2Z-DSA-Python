'''
Coding Ninja > https://www.codingninjas.com/studio/problems/longest-successive-elements_6811740?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
Leetcode > https://leetcode.com/problems/longest-consecutive-sequence/editorial/

Problem Statement: You are given an array of 'N' integers. 
You need to find the length of the longest sequence which contains the consecutive elements.
Example :
Input: [100, 200, 1, 3, 2, 4]
Output: 4
Explanation: The longest consecutive subsequence is 1, 2, 3, and 4.
'''

# Brute Force 
def consecutive_bf(a):
    n = len(a)
    # Sorting the array in ascending order 
    for i in range (n):
        for j in range (i+1,n):
            if a[i] > a[j]:
                a[i], a[j] = a[j],a[i]
    # a.sort() 
    '''
    we can just use sort method to sort the array which brings the timecomplexity to  O(n log N) for O(n^2)
    '''
    # Now checking for longest consectuive 
    count  = 1
    max_count = 1 
    for ele in range  (1,n):
        if (a[ele] - a[ele-1]) == 1: 
            count +=  1
        elif a[ele] != a[ele-1]: 
            count = 1 
        if max_count < count :
            max_count = count        
    return max_count


# Optimal Approach 
def consecutive(a):
    n = len(a)
    count = 1
    max_count = 0
    no_dupli = set()
    for i in range (n):
        no_dupli.add(a[i])
        
    for i in range (n):
        if a[i] in no_dupli :
            currentEle = a[i]
            
        while currentEle in no_dupli :
            currentEle += 1
            
        curLen = currentEle - a[i] + 1
    max_count = max(max_count,curLen)
    
    return max_count
    
# Test Run 
print (consecutive( [15, 6, 2, 1, 16, 4, 2, 29, 9, 12, 8, 5, 14, 21, 8, 12, 17, 16, 6, 26, 3]))