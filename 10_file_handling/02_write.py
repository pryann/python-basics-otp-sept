with open("example.txt", "w", encoding="UTF-8") as f:
    f.write("Ollé")

text = ["first\n", "second\n", "third"]
with open("example2.txt", "w", encoding="UTF-8") as f:
    f.writelines(text)
