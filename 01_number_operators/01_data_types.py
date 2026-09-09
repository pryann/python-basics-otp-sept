# numbers: int, float, complex
# string: str
# boolean: bool
# None: NoneType

# int
print(1000)
print(10e10)
print(-1000)

# float: IEEE 754
print(12.123)
print(12.1e-12)
print(1.79e308, type(1.79e308))  # max
print(1.8e308, type(1.8e308))  # inf
print(5e-324, type(5e-324))  # cloesest non zero
print(1e-325, type(1e-325))  # zero

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3) # False
