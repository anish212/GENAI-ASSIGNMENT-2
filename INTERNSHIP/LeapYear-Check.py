year = int(input("Enter a year: "))


is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if is_leap:
    print(f"{year} is a Leap year.")
    if year % 400 == 0:
        print("Reason: It is divisible by 400.")
    else:
        print("Reason: It is divisible by 4 but not by 100.")
else:
    print(f"{year} is NOT a leap year.")
    print("Reason: It doesn't meet the leap year criteria.")