'''

Convert a Given valid mathemitical expression to Prefix from Infix


'''


def infixToPrefix(exp):
    
    
    weights = {"+":1,"-":1, "*":2,"/":2, "^":3}
    result = [] 
    op = [] 
   
    
    # Reverse the infix expression and swap parantheses 
    exp = exp[::-1]
    exp = exp.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    
    for char in exp:
        if char.isalnum() :
            result.append(char)
            
        elif char == ")":
            op.append(char)
        
        elif char == "(" :
            
            while op and op[-1] != ")" :
                result.append(op.pop())
            
            if op and op[-1] == ")":
                op.pop() 
                
        else:
            
            while op and op[-1] != ")" and weights.get(char,0) < weights.get(op[-1],0):
                result.append(op.pop())
            op.append(char)
            
    while op :
        result.append(op.pop())
        
    return "".join(result[::-1])



a =  "a+b"
# a =  "x+y*z/w+u"
print(infixToPrefix(a))
            
        