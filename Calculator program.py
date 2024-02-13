operator = input("Enter the operator(+ - * /): ")
a = float(input("Enter the a value: "))
b = float(input("Enter the b value: "))
if operator == '+':
    print("Addition",a+b)
elif operator == '-':
    print("Subtraction",a-b)
elif operator == '*':
    print("Multiplication",a*b)
elif operator == '/':
    print("Division",a/b)
else:
    print("operator is valid")

