def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Div by Zero"
def modulus(a, b): return a % b
def power(a, b): return a ** b

def calculator():
    while True:
        print("\n1. Add 2. Sub 3. Mul 4. Div 5. Mod 6. Pow 7. Exit")
        choice = input("Enter choice: ")
        if choice == '7': break
        
        x = float(input("First num: "))
        y = float(input("Second num: "))
        
        if choice == '1': print(add(x, y))
        elif choice == '2': print(subtract(x, y))
        elif choice == '3': print(multiply(x, y))
        elif choice == '4': print(divide(x, y))
        elif choice == '5': print(modulus(x, y))
        elif choice == '6': print(power(x, y))

calculator()