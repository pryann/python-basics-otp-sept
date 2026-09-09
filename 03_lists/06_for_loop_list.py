yearly_salaries = [
    120_000,
    72_000,
    57_000,
    98_000,
]

for i in yearly_salaries:
    print(i)

# i is not the real index, but it is match with the list item idex
for i in range(len(yearly_salaries)):
    print(f"index: {i}, value: {yearly_salaries[i]}")

#  better solution, 'i' is generated
for i, v in enumerate(yearly_salaries):
    print(f"index: {i}, value: {v}")
