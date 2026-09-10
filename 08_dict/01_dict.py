# ordered, mutable, no duplicated members
# key can any immutable type

user = {
    "name": "John Doe",
    "age": 33,
}

print(user)
print(user["name"])
print(user["age"])

user["status"] = "dead"
print(user)

user.pop("status")
print(user)

user.update({"job": "writer", "age": 22})
print(user)
