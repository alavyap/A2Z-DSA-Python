# Example 1
age =  10 

if(age >= 18):
    print("You are an adult.")
else :
    print("You are not an adult.")
    
# Output : You are not an adult.

# -----------------------------------------------------
# Example 2

marks = 54

if (marks < 25):
    print("Grade: F")
elif (marks >= 25 and marks <= 44):
    print("Grade: E")
elif(marks >=45 and marks <=49):
    print("Grade: D")
elif(marks >= 50 and marks <= 59):
    print("Grade: C")
elif(marks >= 60 and  marks <= 69):
    print("Grade: B")
elif(marks >= 70):
    print("Grade: A")
else:
    print("Invalid Marks Entered.")
    
# Output : Grade: C
# -----------------------------------------------------
# Example 3


marks = 54
grade= " "   # right now grade is empty 

if (marks < 25):
    grade= "F"
elif ( marks <= 44):
    grade= "E"               
elif(marks <=49):
    grade= "D"
elif(marks <= 59):
    grade= "C"
elif( marks <= 69):
    grade= "B"
elif(marks >= 70):
    grade= "A"
else:
    grade = "X"

print("Grade:",grade)
    