# global fn

print(len("Gergely"))

# methods
name = "gergely"
print(name[0])
print(name[6])
# str is immutable
# TypeError: 'str' object does not support item assignment
# name[0] = "A"

# print(f"capitalized: {name.capitalize()}")
print("capitalized: ", name.capitalize())
print("uppercase: ", name.upper())
print("all character are lowercase: ", name.islower())
print("find index of 'g': ", name.find("g"))
print("count of 'g': ", name.count("g"))
print("replace 'e' to 'E': ", name.replace("e", "E"))
print("remove leading spaces: ", "   Gergely               s     ".strip())
