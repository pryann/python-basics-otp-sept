global_value = "global value"

print(global_value)


def log_global():
    # we can access the global_value
    global global_value
    global_value = "GLOB"
    local_value = "local value"
    print(local_value)
    print(global_value)


log_global()

print(global_value)

# NameError: name 'local_value' is not defined.
# print(local_value)
