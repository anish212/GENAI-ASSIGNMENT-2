def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total = total + int(digit)
    return total

def reverse_number(n):
    s = str(n)
    return int(s[::-1])

num = int(input("Enter a number to analyze: "))
print("Sum of digits:", sum_of_digits(num))
print("Reversed number:", reverse_number(num))