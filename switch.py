day = 4 

match (day):
    case 1: 
        print("Monday")
        
    case 2: 
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")
        
# -----------------------------------------------------

# Example 2 
x = 10
y = 5

match (x + y ) :
    case 15:
        print("Result is 15.")
    case 20: 
        print("Result is 20.")
    case _ :   # in python this is the way to write default case.
        print("No match found.")

#------------------------------------------------------------------------------------

# Example 3
grade = 'B'

match (grade):
    case 'A':
        print("Excellent!")
    case 'B':
        print("Good!")
    case _ : 
        print("Not specified.")

# ---------------------------------------------

# Example 4
day = 2 

match (day):
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
        
    case 2:   # In Python the duplicate case is not allowed
        print("Duplicate Case.")
        
    case _ :
        print("Invalid day.")
        
# ---------------------------------------------------------------------------

# Example 5

x = 2 
y = 3

match (x):
    case 1 : 
        print("x is 1.")
        
        # nested switch 
        match (y):
            case 1 :
                print("y is 1.")
            case _ :
                print("y is not 1.")
    
    case _ :
        print("x is not 1.")
        

from typing import *

def areaSwitchCase(ch: int, a: List[float]):
    
    match ch:
        case 1: 
            return ((22/7) *a[0]*a[0])
        case 2 :
            return( a[0] * a[1])
        case _ :
            return ("Invalid")

# Example usage
result = areaSwitchCase(1, [5.0])
print(result)
