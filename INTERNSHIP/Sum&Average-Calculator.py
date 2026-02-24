count = int(input("How many numbers? "))
nums = []

for i in range(count):
    val = float(input(f"Enter number {i+1}: "))
    nums.append(val)

if nums:
    print(f"Sum: {sum(nums)}")
    print(f"Average: {sum(nums)/len(nums)}")
    print(f"Maximum: {max(nums)}")
    print(f"Minimum: {min(nums)}")