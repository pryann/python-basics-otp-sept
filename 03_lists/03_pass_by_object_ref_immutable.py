age = 30
age_copy = age

# -----------
# 0x000A 30   <---- age
#             <---- age_copy
# -----------

print(age, id(age))
print(age_copy, id(age_copy))

age = 18
print(age, id(age))
print(age_copy, id(age_copy))
# -----------
# 0x000A 30   <---- age_copy
# -----------
# 0#000B 18   <---- age
# -----------