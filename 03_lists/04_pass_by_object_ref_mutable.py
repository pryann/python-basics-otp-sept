yearly_salaries = [
    120_000,
    72_000,
    57_000,
    98_000,
]

yearly_salaries_copy = yearly_salaries

# ------------------
# 0x000A
# [
#     120_000,          <------- yearly_salaries
#     72_000,           <------- yearly_salaries_copy
#     57_000,
#     98_000,
# ]
# -----------------

print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))

yearly_salaries.append(1_000_000)
# ------------------
# 0x000A
# [
#     120_000,          <------- yearly_salaries
#     72_000,           <------- yearly_salaries_copy
#     57_000,
#     98_000,
#     1_000_000
# ]
# -----------------
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))

yearly_salaries = [1, 2, 3]
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))
# [
#     120_000,
#     72_000,           <------- yearly_salaries_copy
#     57_000,
#     98_000,
#     1_000_000
# ]
# -----------------
#  0x000B
#  [1, 2, 3]            <------- yearly_salaries
# ----------------

a = [1, 2, 3]
b = a.copy()
print(id(a))
print(id(b))
