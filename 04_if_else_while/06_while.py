for i in range(10):
    print(i)


i = 0
while i < 10:
    print(i)
    i += 1

# falsy values: 0, None, False, '', [], {},
# truthy values: any non-zero number, any non-empty string, any non-empty list, any non-empty dictionary
while True:
    grade = input("Adj meg egy jegyet (1-5): ")
    if grade.isdigit() and 0 < int(grade) < 6:
        print("Ez egy érvényes jegy")
        break
    print("Érvénytelen jegy")
