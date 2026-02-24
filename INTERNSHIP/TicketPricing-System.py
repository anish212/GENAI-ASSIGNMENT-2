age = int(input("Enter age: "))
day = input("Enter day of week: ").lower()
qty = int(input("Number of tickets: "))

if age < 3: base = 0
elif 3 <= age <= 12: base = 150
elif 13 <= age <= 59: base = 300
else: base = 200

discount = 0
if day in ['friday', 'saturday', 'sunday']:
    discount = 0.20 * base

final_unit_price = base - discount
total = final_unit_price * qty

print(f"\nBase Price: ₹{base}")
print(f"Discount: ₹{discount}")
print(f"Price after discount: ₹{final_unit_price}")
print(f"Total Amount: ₹{total}")