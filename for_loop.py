'''
                        In Python the for loop can take 3 inputs that are :
                            for i {initialize} in range (start, end, step/difference)
                            start => Generally starts for 0
                            end => Generally ends at the upper limit
                            step => Generally it is 1
'''
# Example 1 
for i in range (11): 
    print("Hey, Striver, this is the {}'th iteration".format(i))
    
# -------------------------------------------------------------------------------------------------------------------------

# Example 2
for i in range (3):
    for j in range (3):
        print("i = {} , j = {}".format(i,j))
        
# -----------------------------------------------------------------------------

# Example 3
for i in range (1,25,5):
    print("i = {}".format(i))
    
    
    