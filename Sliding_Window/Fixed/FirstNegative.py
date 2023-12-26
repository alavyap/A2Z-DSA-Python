'''
Given an array and a positive integer k, find the first negative integer for each and every window(contiguous subarray) of size k.
Print 0 if there is not negative number

Input:
2
5
-8 2 3 -6 10
2
8
12 -1 -7 8 -15 30 16 28
3

Output:
-8 0 -6 -6
-1 -1 -7 -15 -15 0 . 

'''






def firstNegative(arr,k):
    
    n = len(arr)
    def windowNegative(window):
        if window:
            return window[0]
        else:
            return 0
        
    result = []
    
    for i in range (n-k +1):
        window = arr[i:i +k]
        neg_window = []
        for num in window:
            if num < 0:
                neg_window.append(num)     
        result.append(windowNegative(neg_window))
    return result
    

# Test Run
print(firstNegative([12,-1,-7,8,-15,30,16,28],3))
print(firstNegative([-8,2,3,-6,10],2))