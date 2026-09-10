with open("text.txt", "r", encoding="UTF-8") as f:
    print(f.read())
    f.seek(0)
    print(f.read())
    f.seek(0)
    print(f.readline())
    f.seek(0)
    print(f.readlines())
    f.seek(0)
    for line in f:
        print(line, end="")
    # advanced tech, and best practice: use generators

