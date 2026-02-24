def temp_menu():
    print("\n1. C to F | 2. F to C | 3. C to K | 4. K to C | 5. F to K | 6. K to F | 7. Exit")
    choice = input("Choice: ")
    
    if choice == '7': return False
    
    temp = float(input("Enter temperature value: "))
    
    if choice == '1': print(f"Result: {(temp * 9/5) + 32} F")
    elif choice == '2': print(f"Result: {(temp - 32) * 5/9} C")
    elif choice == '3': print(f"Result: {temp + 273.15} K")
    elif choice == '4': print(f"Result: {temp - 273.15} C")
    elif choice == '5': print(f"Result: {(temp - 32) * 5/9 + 273.15} K")
    elif choice == '6': print(f"Result: {(temp - 273.15) * 9/5 + 32} F")
    
    return True

while temp_menu(): pass