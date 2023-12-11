'''
Problem: Print from N to 1 using Recursion

'''
# This is my approach 

def printNos(x):
    i =1
    if i >x :
        return
    print(x,end=" ")
    printNos(x-1)
    
printNos(5)

# Coding Ninja's Approach

def reverseFunc(x,ans):
    if x == 0:
        return 
    ans.append(x)  # this line should be above as first it will append the x then it will change the value of x for the next step, 
    # if this will be below then it will save like this[1,2,3,4,5]
    reverseFunc(x-1,ans)
def printNos(x):
    ans =[]
    
    reverseFunc(x,ans)
    
    return ans

print(printNos(5))


