marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

total = sum(marks)
percentage = (total / 500) * 100

if percentage >= 90: grade = "A+ (Outstanding)"
elif percentage >= 80: grade = "A (Excellent)"
elif percentage >= 70: grade = "B (Good)"
elif percentage >= 60: grade = "C (Average)"
elif percentage >= 50: grade = "D (Pass)"
else: grade = "F (Fail)"

passed_all = all(m >= 40 for m in marks)
result = "Pass" if (passed_all and percentage >= 50) else "Fail"

print(f"\nTotal Marks: {total}/500")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
print(f"Result: {result}")