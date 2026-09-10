yearly_salaries = [10_000, 15_000, 20_000, 25_000, 30_000, 40_000, 50_000, 60_000]

print("to the 2.: ", yearly_salaries[:2])
print("from the 2.: ", yearly_salaries[2:])
print("from the 2. to the 4.: ", yearly_salaries[2:4])
print("every second element: ", yearly_salaries[::2])
print("every second element from the 2. to 6.: ", yearly_salaries[2:6:2])
print("last element: ", yearly_salaries[-1])
print("second last element: ", yearly_salaries[-2])
print("reverse list: ", yearly_salaries[::-1])

yearly_salaries_copy = yearly_salaries[:]
print(id(yearly_salaries))
print(id(yearly_salaries_copy))
