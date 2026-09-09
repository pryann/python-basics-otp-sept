numbers = [
    1,
    2,
    43,
    5,
    21,
    54,
    74655,
    3,
    4,
    364,
    8,
    3,
    2,
    45,
    567,
]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)


yearly_salaries = [120_000, 72_000, 57_000, 98_000, 101_000, 22_000, 1_123_000]
high_salary_treshold = 70_000
sum_high_salaries = 0

for salary in yearly_salaries:
    if salary > high_salary_treshold:
        sum_high_salaries += salary

print(sum_high_salaries)
