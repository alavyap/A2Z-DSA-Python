'''
Problem Description:
Given an array containing N positive integers and an integer K. Your task is to find the length of the longest Sub-Array with sum of the elements equal to the given value K.

For Input:
1
7 5
4 1 1 1 2 3 5
your output is: 
4 . 
'''

def longest_subarray_sum(arr,k):
    
    # this dictionary will store the prefix sum and its corresponding index
    prefix_sum = {0:-1}
    current_sum = 0
    max_length = 0
    n = len(arr)
    
    # the for loop will run till length of array that is n
    for i in range (n):
        current_sum += arr[i]
        
    # check if (current_sum -k) is present in the prefix sun dictionary
    
        if (current_sum -k) in prefix_sum :
            # max_length = max(max_length, i-prefix_sum[current_sum -k])
            if max_length < (i-prefix_sum[current_sum -k]):
                max_length = (i-prefix_sum[current_sum -k])
            else :
                continue
            
        # if the current sum is not present in the prefix sum dictionary, add it with its index
        if (current_sum -k ) not in prefix_sum:
            prefix_sum[current_sum]= i
            
    return  max_length 


# Test Run
print (longest_subarray_sum([4,1,1,1,2,3,5],5))