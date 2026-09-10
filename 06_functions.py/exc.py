# 1. Írj egy Python függvényt, amely visszaadja az adott stringben található szavak számát!


def words_count(text):
    return len(text.split())


# 2. Írj egy függvényt, amely egy lista számokat kap bemenetként, majd visszatér egy új listával, amelyben a számok a kétszeresükkel vannak helyettesítve.


def double_list(numbers):
    return [i * 2 for i in numbers]


# 3. Készíts egy függvényt, amely paraméterként kap két listát és visszaadja azt a listát, amely csak azokat az elemeket tartalmazza, amelyek mindkét listában szerepelnek! Comprehensiont használj!


def get_common_elements(list1, list2):
    # can be more precise, get list lengths
    return [i for i in list1 if i in list2]


# 4. Készíts egy függvényt, amely meghatározza, hogy egy szám prím-e vagy sem!
#    A függvény paraméterként egy számot kap a visszatérési érték pedig bool típusú érték.
def get_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
