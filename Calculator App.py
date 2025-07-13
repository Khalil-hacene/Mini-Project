# Calculator program 
while True:
    operator = input("Enter an operator ('+' '-' '*' '/' '**' '%'): ")
    num1 = float(input("Enter the First number: "))
    num2 = float(input("Enter the Second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print(f"You can't divide by {num2}")
            continue 
        result = num1 / num2
    elif operator == "**":
        result = num1 ** num2
    elif operator == "%":
        result = num1 % num2
    else:
        print(f"You did put the wrong {operator} please select one of this ('+' '-' '*' '/' '**' '%')")
    
    print(round(result, 4))

    if input("if you wanna calcute again enter (y/n): ") == "n":
        break
