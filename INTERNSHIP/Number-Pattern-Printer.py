pattern = int(input("Choose Pattern (1-4): "))
h = int(input("Enter height: "))

if pattern == 1:
    for i in range(1, h + 1):
        for j in range(1, i + 1): print(j, end="")
        print()
elif pattern == 2:
    for i in range(1, h + 1):
        print(str(i) * i)
elif pattern == 3:
    for i in range(h, 0, -1):
        for j in range(i, 0, -1): print(j, end="")
        print()
elif pattern == 4:
    for i in range(1, h + 1):
        # Ascending
        for j in range(1, i + 1): print(j, end="")
        # Descending
        for j in range(i - 1, 0, -1): print(j, end="")
        print()