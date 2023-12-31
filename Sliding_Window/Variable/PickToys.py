'''
John is at a toy store help him pick maximum number of toys. He can only select in a continuous manner and he can select only two types of toys.

Example:
Input:
1
abaccab
Output: 4{acca} 

'''

from re import A


def pickToy(arr):
    n = len(arr)
    # to store the last index of each character
    toy_count = {}
    left = 0
    max_toys = 0
    
    for right in range (n):
        # update character count in the current window
        toy_count[arr[right]] = toy_count.get(arr[right],0) + 1
        
        # check if the toys is unique
        while len(toy_count) > 2 :
            toy_count[arr[left]] -= 1 
            # remove a character from the left end if it's no longer needed
            if toy_count[arr[left]] == 0 :
                del toy_count[arr[left]]
            left += 1
            
        # update the max_toys 
        if max_toys < (right - left + 1):
            max_toys = right - left  + 1
    return max_toys


# Test Run 
print(pickToy("abaccab"))   # Output:4