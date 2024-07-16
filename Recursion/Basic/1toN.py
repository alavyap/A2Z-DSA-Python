'''
You are given an interger 'n'
Return an array containing integers from 1 to n (in increasing order) without using loops.
The time complexity of the code is O(n) because the function give_array will run for n times 

'''
# My Approach : This will not work in coding ninja as it is expecting a list not just integers
def printNos(n, i= 1):
    if(i >n):
        return
    print(i,end= " ")
    printNos(n, i+1)
printNos(5)
 
# Coding Ninja (Python 3.5)
def recursionFun(x,ans):
# The function that does the main work
    if x == 0:
        return
    recursionFun(x-1,ans)
    ans.append(x)
    

def printNos(x: int) : 
    # Write your code here
    
    ans = []
    recursionFun(x,ans)
    
    return ans