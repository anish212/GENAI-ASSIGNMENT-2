balance = 10000
min_balance = 500

while True:
    print("\nATM SIMULATOR\n1. Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        print(f"Current Balance: ₹{balance}")
    elif choice == '2':
        amt = float(input("Enter deposit amount: "))
        balance += amt
        print(f"Success! New balance: ₹{balance}")
    elif choice == '3':
        amt = float(input("Enter withdrawal amount: "))
        if balance - amt < min_balance:
            print("Failed: Must maintain minimum ₹500.")
        else:
            balance -= amt
            print(f"Success! New balance: ₹{balance}")
    elif choice == '4':
        break
    else:
        print("Invalid choice.")