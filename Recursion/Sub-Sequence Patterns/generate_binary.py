'''
GFG :> https://www.geeksforgeeks.org/generate-binary-strings-without-consecutive-1s/

Given an integer, K. Generate all binary strings of size k without consecutive 1’s.

Examples: 
Input : K = 3  
Output : 000 , 001 , 010 , 100 , 101 
Input : K  = 4 
Output :0000 0001 0010 0100 0101 1000 1001 1010

Idea behind that is IF string ends with ‘1’ then we put only ‘0’ at the end. IF string ends with ‘0’ then we put both ‘0’ and ‘1’ at the end of string for generating new string.


'''
# Recursive Method 
def generate(k):
    if k <= 0 :
        return 
    
    str = [0] * k  #this is a string of size k which will store the value of k
    
    str[0] = '0'
    generateBin(k,str,1)
    
    str[0] = '1'
    
    generateBin(k,str,1)


def generateBin(k,str,n):
    if n ==k  :
        print (*str[:n],sep= " ", end = " ")
        return 
    
    
    if str[n-1] == '1' :
        str[n] = '0'
        
        generateBin(k,str,n +1)
        str[n] = '1'
        generateBin(k,str,n+1)
        
        
# Time Complexity :.. O(2^K) ,where k is hte size of the binary string 
# Space Complexity :. O(K)

'''
The above approach can also be solved using string. It does not have any effect on complexity but string handling, printing and operating is easy.
'''

def mainS(k):
    word = ""
    word += '0'
    all_Binary(word,k)
    word = '1'
    all_Binary(word,k)
    
    
def all_Binary(str,num):
    n = len(str)
    
    if n == num :
        print(str,end=" ")
        
    elif (str[n-1] == '1'):
        all_Binary(str+'0',num)
        
    else :
        all_Binary(str+ '0',num)
        all_Binary(str + '1',num)


# Time Complexity: O(2^n)
# Auxiliary Space: O(n)


# Other Method of Recursive way of solving the same problem 
def generateBinary(k):
    if k == 0 :
        return 
    if k == 1 :
        return ['0' , '1']
    
    result = [] 
    
    for s in generateBinary(k-1):
        result.append(s + '0')
        if s[-1] != '1':
            result.append(s + '1')
            
    return result

'''
Time Complexity: O(2n), where n is the length of the binary strings to be generated.
Auxiliary Space: O(2n) because at any point in time, the function stores all the binary strings generated so far in the result list, and as the number of strings generated is 2n, the space required to store them is also 2n.
'''