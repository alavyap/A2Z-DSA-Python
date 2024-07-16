'''
You are given an array. The task is to reverse the array and print it. 

'''
def reverseArray(n,nums):
    if n==0:
        return
    for i in range (0, n//2):
        temp = nums[i]
        nums[i] = nums[len(nums)-1-i]
        nums[len(nums)-1-i] = temp
    return nums

# Testing the function
print(reverseArray(6,[1,2,3,4,5,6]))