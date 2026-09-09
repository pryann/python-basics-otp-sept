prog_lang = "Java"

# A   B   A or B
# 0   0      0
# 0   1      1
# 1   0      1
# 1   1      1

# BAAAAD, UGLYYYYY
if prog_lang == "Java" or prog_lang == "Python":
  print("Backend")

backend_languages = ["java", "python"]
if prog_lang.lower() in backend_languages:
  print("backend")

# A   B   A and B
# 0   0      0
# 0   1      0
# 1   0      0
# 1   1      1
age = 30
if age < 18:
  print("Kiskorú")
# elif age >= 18 and age < 65:
elif 18 <= age < 65:
  print("Felnőtt")
else:
  print("Nyugdíjas")


temperature = 50
humidity = 60
rain = True

# not rain            False
# humidity < 70       True
#                     False and True  =  False
# temperature > 30    True
#                     False or True   =   True

if temperature > 30 or humidity < 70 and not rain:
    print("Dry")

# temperature > 30    True
# humidity < 70       True
#                     True or True     =  True
# not rain            False
#                     True and False   =  False

if (temperature > 30 or humidity < 70) and not rain:
    print("Dry")

