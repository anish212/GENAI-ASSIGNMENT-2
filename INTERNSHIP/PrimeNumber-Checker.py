def check_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

num = int(input("Enter a number to check: "))
print(f"{num} is {'a PRIME' if check_prime(num) else 'NOT a PRIME'} number.")

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))
primes = [x for x in range(start, end + 1) if check_prime(x)]
print(f"Prime numbers: {primes}")