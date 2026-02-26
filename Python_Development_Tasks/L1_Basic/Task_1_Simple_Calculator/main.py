from os import system
from time import sleep
# def divide(x, y):
#     try:    
#         return x/y 
#     except ZeroDivisionError:
#         return "Error: Divided by zero"
    
add = lambda x,y: x+y 
subtract = lambda x,y: x-y
multiply = lambda x,y: x*y 
divide = lambda x,y: "Divided by zero" if y == 0 else x/y 

quit = ""

while quit != 'q': 
    system('cls' if system == 'nt' else 'clear')
    print("A CLI calculator\n")
    try: 
        x = float(input("Enter value of X: "))
        y = float(input("Enter value of Y: "))
    except Exception as e:
        continue
    operator = input("Select an operation (+, -, *, /): ").strip()
    print("\nResult: ", end="")
    if operator[0] == "+":
        print(add(x,y))
    elif operator[0] == "-":
        print(subtract(x,y))
    elif operator[0] == "*":
        print(multiply(x,y))
    elif operator[0] == "/":
        print(divide(x,y))
    else:
        print("Invalid operation")
        
    quit = input("\nPress any key to continue or 'q' to exit: ").strip().lower()