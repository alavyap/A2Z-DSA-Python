'''
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
    '''
    # Brute Force 
    ans = 1 
    for i in range (1,n):
        ans= ans * (n-i)
        ans = ans // (i)
        print (ans,end= ",")
    '''
    # Optimal Approach  Time Complexity = O(n*r) Space Complexity = O(1)
    for c in range (1,n+1):
        print(nCr(n-1,c-1),end=" ")
    print()
# Test Run
# twoPascals(5,5,3)

# Varient 3 Optimal Code 
def threePascal(N,r,c):
    ans = [] 
    for row in range (1,N+1):
        temp = [] 
        for col in range (1,row+1):
            temp.append(nCr(row-1,col-1))
        ans.append(temp)
    return ans 

# Test Run 
print(threePascal(5,5,3))
        
    