n = int(input("Enter a number: "))

if n < 0:
    print("Factorial not defined for negative numbers.")
elif n == 0:
    print("0! = 1")
else:
    fact = 1
    steps = ""
    for i in range(n, 0, -1):
        fact *= i
        steps += str(i) + (" × " if i > 1 else "")
    print(f"{n}! = {steps} = {fact}")