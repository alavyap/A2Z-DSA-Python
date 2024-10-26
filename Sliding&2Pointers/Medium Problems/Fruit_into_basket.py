'''

Geeks For Geeks :> https://www.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/1

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array of arr[], where arr[i]  is the type of fruit the ith tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow :

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of the baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array of fruits, return the maximum number of fruits you can pick.

Examples:

Input: arr[]= [2, 1, 2]
Output: 3
Explanation: We can pick one fruit from all three trees. Please note that the type of fruits is same in the 1st and 3rd baskets.

Input: arr[] = [3, 1, 2, 2, 2, 2]
Output: 5
Explanation: It's optimal to pick from the last 5 trees. Please note that we do not pick the first basket as we would have to stop at thrid tree which would result in only 2 fruits collected.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] <=n


'''
#  we need a map 
def total (arr):
    n = len(arr)
    left =  0 
    f_count = {} 
    maxi = 0 
    
    
    for right in range (n):
        f_type = arr[right]
        
        if f_type in f_count :
            f_count[f_type] += 1 
        else :
            f_count[f_type] = 1  
            
            
        while len(f_count) > 2 :
            left_f_type = arr[left]
            f_count[left_f_type] -=1 
            if f_count[left_f_type] == 0 :
                del f_count[left_f_type] 
            left += 1 
        maxi = max( maxi , right - left +1 )
    
    return maxi
   
        


arr = [2,1,2]
print(total(arr))