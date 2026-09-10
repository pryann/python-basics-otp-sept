user = {
    "name": "John Doe",
    "age": 33,
    "job": "writer",
}

for i in user:
    print(i)

print("keys: ", user.keys())
print("values: ", user.values())
print("items: ", user.items())

for i in user.values():
    print(i)

for k, v in user.items():
    print(k, v)
