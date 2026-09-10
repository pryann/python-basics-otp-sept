def gcd(a: int, b: int) -> int:
    return a if b == 0 else gcd(b, a % b)


print(gcd(12, 8))
print(gcd(11, 33))
