# CRUD: Create Read Update Delete

from users import users


def generate_id(users):
    # max_id = 0
    # for user in users:
    #     if user["id"] > max_id:
    #         max_id = user["id"]
    # return max_id + 1
    # return max([user["id"] for user in users]) + 1
    return max(user["id"] for user in users) + 1


def find_user_by_id(id):
    for user in users:
        if user["id"] == id:
            return user
    # return None


# print(find_user_by_id(2))


def update_user(id, payload):
    user = find_user_by_id(id)
    # if user is not None:
    if user:
        user.update(payload)
        return user


# print(update_user(1, {"first_name": "Bubu"}))


def create_user(payload):
    # v1
    # payload.update({"id": generate_id(users)})
    # users.append(new_user)
    # v2
    # new_user = {"id": generate_id(users)}
    # new_user.update(payload)
    # users.append(new_user)
    # v3
    users.append({"id": generate_id(users), **payload})
    return users[-1]


# print(
#     create_user(
#         {"first_name": "Fanni", "last_name": "Kiss", "email": "kissfanni@gmail.com"},
#     )
# )


def remove_user(id):
    user = find_user_by_id(id)
    if user:
        users.remove(user)
        return True
    return False


print(remove_user(1))
print(users)
