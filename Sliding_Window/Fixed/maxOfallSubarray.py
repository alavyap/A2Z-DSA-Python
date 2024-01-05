'''
>>>> This question is of QUEUE data structure
Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.

Example:
Input 1:
    A = [1, 3, -1, -3, 5, 3, 6, 7]
    B = 3
Output 1:
    C = [3, 3, 5, 5, 6, 7] . 
'''

from collections import deque
def queueMax(arr,l):
    # length of the arr
    N= len(arr)
    
    # Initialize a deque to store the indices of elements in the current winodw
    window = deque()
    
    # Array to store the maximum for  each subarray of size l
    result = []
    
    # process the first K elements seperately
    for i in range (l):
        
        # Remove elements smaller than the current element from the back of the deque
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        window.append(i)
        
    # Process the remaining elements
    for i in range (l,N):
            
        result.append(arr[window[0]])
            
        # Remove elements that are outside the current window
        while window and window[0] <= i-l:
            window.popleft()
                
        # Remove elements smaller than the current element from the back of the deque
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        window.append(i)
            
            
        # Append the Maximum element for the last window {subarray}
    result.append(arr[window[0]])
    return result

# Test Run 
print(queueMax([1,3,-1,-3,5,3,6,7],3))