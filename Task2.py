number1=int(input("Enter first number:"))
number2=int(input("Enter second Number:"))

print("Please select operation -\n" \
        "1. Add(+)\n" \
        "2. Subtract(-)\n" \
        "3. Multiply(*)\n" \
        "4. Divide(/)\n" \
        "5. Module(%)\n" \
        "6. Exponent(**)\n" )

operator=input("Enter operator:")

if operator=="+":
    add = number1+number2
    print(f"the addition of {number1} {operator} {number2} is",add)

elif operator=="-":
    subtract=number1-number2
    print(f"the sutraction of {number1} {operator} {number2} is",subtract)

elif operator=="/":
    Div=number1/number2
    print(f"the Division  of {number1} {operator} {number2} is",Div)

elif operator=="%":
    Mod=number1%number2
    print(f"the Module of {number1} {operator} {number2} is",Mod)

elif operator=="**":
    expo=number1**number2
    print(f"the Exponential of {number1} {operator} {number2} is",expo)

else:
    print("Invalid Input")