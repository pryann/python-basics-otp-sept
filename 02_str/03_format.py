first_name = "Gergely"
last_name = "Gáll"

full_name = first_name + " " + last_name
print(full_name)
print(full_name * 3)

name = "John"
age = 33
# My name is John, and I'm 33 years old.
sentence = "My name is " + name + " and I'm " + str(age) + " years old."
print(sentence)
sentence = "My name is {0} and I'm {1} years old.".format(name, age)
print(sentence)
# sentence = f"My name is {name.upper()} and I'm {age + 1} years old."
sentence = f"My name is {name} and I'm {age} years old."
print(sentence)

# pythonban nincs const, de a nagybetűs konvenciót opcionálisan lehet használni
PI = 3.14159
print(PI)

# https://www.w3schools.com/python/ref_string_format.asp
print("The value of pi is {:.2f}".format(PI))

# f string
print(f"The value of pi is {PI:.2f}")

#  tehát NEM konstans
PI = 3.1
print(PI)
