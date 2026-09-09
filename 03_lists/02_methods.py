yearly_salaries = [
    120_000,
    72_000,
    57_000,
    98_000,
]

# elem hozzáfűzése a végéhez
yearly_salaries.append(79_000)
print(yearly_salaries)

# iterable elemeinek a hozzáfűzése a lista végéhez
yearly_salaries.extend([210_000, 99_000])
print(yearly_salaries)

# elem beszűrása adott idnexű helyre
yearly_salaries.insert(2, 222_000)
print(yearly_salaries)

yearly_salaries.remove(222_000)
print(yearly_salaries)

# adott indexű elem törlése, alapértelmezetten az utolsó
yearly_salaries.pop()
print(yearly_salaries)

# törlés index alapján
del yearly_salaries[0]
print(yearly_salaries)

print(yearly_salaries.count(57_000))

yearly_salaries.sort(reverse=True)
print(yearly_salaries)

yearly_salaries.reverse()
print(yearly_salaries)

text = "My name is Gergely Gáll"
text_parts = text.split()
print(text_parts)
concated = " ".join(text_parts)
print(concated)
