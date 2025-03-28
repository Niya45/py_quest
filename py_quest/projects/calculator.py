operator = input("enter an operator (+ - / *):")
num1 = float(input("Enter a number:"))
num2 = float(input("Enter another number:"))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1/num2)
else: 
    print(f"sorry! the operator {operator} isn't in the list!")