def is_prime(n):
    # Step 1: Handle base cases
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n <= 3:
        return True   # 2 and 3 are prime numbers

    # Step 2: Eliminate multiples of 2 and 3 early
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Step 3: Check divisibility using 6k ± 1 optimization
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Check next possible factors in the form of 6k ± 1

    # Step 4: Return True if no divisors found
    return True
