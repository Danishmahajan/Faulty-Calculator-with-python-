print("Enter Your First number. ")
num1 = int(input())
print("Enter the Second number.")
num2 = int(input())
print("Enter the mathematical operation you want to perform (+,-,*,/)")
op = input()
if num1 == 5 and num2 == 2 and op == "*":
    print("15")
elif num1 == 3 and num2 == 4 and op == "+":
    print("10")
elif num1 == 5 and num2 == 6 and op == "/":
    print("60")
elif num1 == 7 and num2 == 5 and op =="-":
    print("6")
elif op == "+":
    print("Addition is : ", num1+num2)
elif op == "-":
    print("Subtraction is :",num1- num2 )
elif op == "*":
    print("Multiplication is :", num1* num2)
elif op == "/":
    print("Dividation is : " ,num1/num2)
else:
    print("Not supported")
    print("Thnks for calculating")



