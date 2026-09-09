print(10 + 20)
# operandus: érték vagy változó, amely részt vesz egy máveletben: 10, 20
# perátor: szimbólum vagy kulcsszó, amely egy máveletet hajt végre az operandusokon: +
# kifejezés: kódrészlet: ami értéket ad vissza

summa = 10 + 20
# utasítás: kódrészlet, amely egy vagy több máveletet hajt végre, de nem ad vissza értéket
# operadus: 10, 20
# operátor: =, +
# kifejezés: 10 + 20
# utasítás: summa = 10 + 20

# dynamic vs static
# static:
#   az adat típus ismert a futtatás előtt
#   a változó típusát a kód írása közben határozzuk meg
#   int age = 10, age:int = 10 (nem feltétlen van kírva, ha ki van akkor explicit is a statikus mellett)
# dinamikus:
#   az adat típus nem ismert a futtatás előtt
#   a típus a program futása során kerül meghatározásra
#   age = 10, type(age)


# explicit vs implict: a forráskódban látható e a típus
# explicit: int age = 10
# inplicit: age = 10

# static and explicit: C++
# fordításkor már ismerjk a típust, és a forráskódban is ki van ír
# a változók típusát meg kell adni kell, és a típusok ellenőrzése a fordítási időben történik
# String name = 'Gáll Gergely'

# static and implicit: Java
# fordításkor már ismert a típus, de nincs kiírva
# a változók típusát nem kell megadni, és a típusellenőrzés futási időben történik
name = "Gáll Gergely"

# dynamic and explicit: Python
# fordításkor nem ismerjük a típust, annak ellenére hogy ki van írva
# a változók típusát egyértelmű módon kell deklarálni, és a típusellenőrzés futási időben történik
# típus annotációról később
vat_rate = int("27")

# dynamic and implicit: JavaScript
# a változók típusa nem kell, hogy egyértelműen módon deklarálva legyen, és a típusellenőrzés is dinamikusan történik a futás során
# a summa típusa a "b" típusától függ
# a = 10
# summa = a + 5
