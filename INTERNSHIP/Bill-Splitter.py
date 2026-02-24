bill = float(input("Enter total bill: "))
people = int(input("Number of people: "))
tax_percent = float(input("Tax percentage: "))
tip_percent = float(input("Tip percentage: "))

tax_amount = (tax_percent / 100) * bill
after_tax = bill + tax_amount
tip_amount = (tip_percent / 100) * bill
total_bill = after_tax + tip_amount
per_person = total_bill / people

print("\n=== BILL BREAKDOWN ===")
print(f"Subtotal: ₹{bill:.2f}")
print(f"Tax ({tax_percent}%): ₹{tax_amount:.2f}")
print(f"After tax: ₹{after_tax:.2f}")
print(f"Tip ({tip_percent}%): ₹{tip_amount:.2f}")
print(f"Total: ₹{total_bill:.2f}")
print(f"Per person: ₹{per_person:.2f}")