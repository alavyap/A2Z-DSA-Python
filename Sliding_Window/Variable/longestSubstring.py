'''
Given a string you need to print the size of the longest possible substring that has exactly k unique characters.
Example:
Input:
2
arr = [aabacbebebe]
k = 3
arr = [aaaa]
k = 1

Output:
7
4 . 
'''

def longest_subString(arr,k):
    n= len(arr)
    char_count = {}
    left = 0
    max_length = 0
    
    for right in range (n):
        # Update character count in the current window
        char_count[arr[right]] = char_count.get(arr[right], 0) + 1 
        
        # shrink the window until it has exactly k unique characters
        while len(char_count) > k :
            char_count[arr[left]] -= 1
            if char_count[arr[left]] == 0 :
                del char_count[arr[left]]
            left += 1
            
        # update the maximum length
        if max_length < (right - left + 1) :
            max_length = (right - left + 1)
            
    return max_length


# Test Run 
test_cases = int(input())
for _ in range(test_cases):
    arr = input().strip()
    k = int(input())
    result = longest_subString(arr, k)
    print(result)
