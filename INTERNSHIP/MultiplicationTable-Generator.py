num = int(input("Enter number: "))
limit = int(input("Enter range (end): "))

print(f"\nMultiplication Table of {num}")
for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")