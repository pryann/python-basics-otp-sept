# * Kérj be két lebegőpontos számot a felhasználótól, majd írasd ki a két szám hányadosát!

number_1 = float(input("Kérem az első számot: "))
number_2 = float(input("Kérem az második számot: "))

print(number_1 / number_2)

# * Adott egy szöveges változó, amiben egy mondat található. Írj programot, ami az összes "_e_" karaktert "_a_"
#   karakterre cseréli a mondatban, ezt tárold el egy új változóban! Írd ki az új értéket!
#   A mondat a következő: "_Lorem ipsum dolor sit amet, consectetur adipiscing elit_"

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
updated_sentence = sentence.replace("e", "a")
print(updated_sentence)

# * Kérj be egy szöveget a felhasználótól, majd írasd ki a hosszát!
text = input("Kérek egy szöveget: ")
print(len(text))
