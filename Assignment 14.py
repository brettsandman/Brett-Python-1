def power(base, exponent):
    """
    Returns base raised to the power of exponent.
    Efficiently handles negative exponents using reciprocal logic.
    """

    # Handle zero exponent: any number to the power of 0 is 1
    if exponent == 0:
        return 1

    # Handle negative exponent: compute reciprocal of the positive exponent result
    if exponent < 0:
        return 1 / power(base, -exponent)

    # Recursive fast exponentiation for positive exponent
    half = power(base, exponent // 2)
    if exponent % 2 == 0:
        return half * half
    else:
        return base * half * half

print(power(2, 3))
print(power(2, -2))
print(power(5, 0))
print(power(3, 4))
