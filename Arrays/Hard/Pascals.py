'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/print-pascal-s-triangle_6917910?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems
LeetCode : > https://www.codingninjas.com/studio/problems/print-pascal-s-triangle_6917910?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems

Problem Statement: This problem has 3 variations. They are stated below:
Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal's triangle.
Variation 2: Given the row number n. Print the n-th row of Pascal's triangle.
Variation 3: Given the number of rows n. Print the first n rows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:
Input Format: N = 5, r = 5, c = 3
Result: 6 (for variation 1)
1 4 6 4 1 (for variation 2)
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1    (for variation 3)

Explanation: There are 5 rows in the output matrix. Each row is formed using the logic of Pascal's triangle.
'''
def nCr(N,r):
    result = 1
    for i in range (r):
        result = result *(N-i)
        result = result// (i+1)   
    return result

# Variation 1  Optimal Approach  Time Complexity = O(c) [C= is given column] Space Complexity = O(1)
def pascals(N,r,c):
    element = nCr(r-1,c-1,)
    return element
# Test Run 
# print(pascals(5,5,3))

# Varient 2  
def twoPascals(n, r, c):
    # Time Complexity = O(n*r) Space Complexity = O(1)
    
    # Brute Force 
    '''
    for c in range (1,n+1):
        print(nCr(n-1,c-1),end=" ")
    print()
    '''
    
    # Optimal Approach 
    ans = 1
    print(ans,end= " ") 
    for i in range (1,n):
        ans= ans * (n-i)
        ans = ans // (i)
        print (ans,end= " ")
    print()
   
# Test Run
# twoPascals(5,5,3)

# Varient 3 
def v3Helper(row):
    result = 1 
    store_ans = [1] 
    for i in range (1,row):
        result *= (row- i)
        result //= (i)
        store_ans.append(result)
    return store_ans

def threePascal(N,r,c):
    ans = [] 
    # Brute Force
    '''
    for row in range (1,N+1):
        temp = [] 
        for col in range (1,row+1):
            temp.append(nCr(row-1,col-1))
        ans.append(temp)
    return ans 
    '''
    # Optimal Approach 
    # Time Complexity = O(n^2) Space Complexity = O(1)
    
    for row in range (1,N+1):
        ans.append(v3Helper(row))
    return ans 
        

# Test Run 
print(threePascal(5,5,3))


# Optimal Approach  

def helper(r):
    result=1
    temp = [1]
    for i in range (r):
        result *= (r-i)
        result //= (i)
        temp.append(result)
    return temp 

def mainfuc(n,r,c):
    # Varient 1 
    '''
    element = helper(r-1,c-1)
    return element 
    '''

    # Varient 2 
    '''
    for c in range (1,n+1):
        print(helper(n-1,c-1),end= " ")
    print ()
    '''
        
    
    #  Varient 3 
    ans = [] 
    for row in range (1,n+1):
        ans.append(helper(row))        
    return ans  


# print(mainfuc(5,5,3))
# (mainfuc(5,5,3)) << This is for varient 2 only