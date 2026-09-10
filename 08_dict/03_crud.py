# CRUD: Create Read Update Delete


from functools import update_wrapper


users = [
    {"id": 1, "first_name": "Bordie", "last_name": "Hartburn", "email": "bhartburn0@slate.com"},
    {"id": 2, "first_name": "Rani", "last_name": "Bradane", "email": "rbradane1@marriott.com"},
    {"id": 3, "first_name": "Maggy", "last_name": "Graybeal", "email": "mgraybeal2@disqus.com"},
    {"id": 4, "first_name": "Marcelle", "last_name": "Sapena", "email": "msapena3@ycombinator.com"},
    {"id": 5, "first_name": "Denyse", "last_name": "Cannon", "email": "dcannon4@chicagotribune.com"},
    {"id": 6, "first_name": "Jacquelynn", "last_name": "Cowans", "email": "jcowans5@army.mil"},
    {"id": 7, "first_name": "Asher", "last_name": "Kos", "email": "akos6@ycombinator.com"},
    {"id": 8, "first_name": "Brynn", "last_name": "Umpleby", "email": "bumpleby7@uol.com.br"},
    {"id": 9, "first_name": "Raeann", "last_name": "Binnall", "email": "rbinnall8@fda.gov"},
    {"id": 10, "first_name": "Frannie", "last_name": "Nulty", "email": "fnulty9@is.gd"},
]


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
