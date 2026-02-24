birth_year = int(input("Enter your birth year: "))
current_year = 2026

age = current_year - birth_year

months = age * 12
days = age * 365
hours = days * 24
minutes = hours * 60
until_100 = 100 - age

print("Current age:", age)
print("Age in months:", months)
print("Age in days:", days)
print("Age in hours:", hours)
print("Age in minutes:", minutes)
print("Years until age 100:", until_100)