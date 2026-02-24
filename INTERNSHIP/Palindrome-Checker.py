entry = input("Enter word/number: ")
clean_entry = str(entry).lower()
reversed_entry = clean_entry[::-1]

print(f"Original: {entry}")
print(f"Reversed: {entry[::-1]}")

if clean_entry == reversed_entry:
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")