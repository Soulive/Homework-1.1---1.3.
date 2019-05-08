# Calculator

text = "Enter two numbers to do calculation"
print (text)

First_number = int(input())
Operation = input("")
Second_number = int(input())

if Operation == "+":
    print(First_number + Second_number)

elif Operation == "-":
    print (First_number - Second_number)

elif Operation == "*":
    print(First_number * Second_number)

elif Operation == "/":
    print (First_number / Second_number)

else: "Error"


