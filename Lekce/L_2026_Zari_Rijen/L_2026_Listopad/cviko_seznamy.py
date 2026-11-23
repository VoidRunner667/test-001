import math
# proměnné a řetězce
jmeno = "Petr"
vek = 25
print(f"Jmenuji se {jmeno} a je mi {vek} let.")

numbers = [1, 2, 3, 4, 5]

numbers.append(6)
numbers.sort()
print(f"Seřazeno seznam: {numbers}")
print(f"Prvni prvek seznamu: {numbers[0]}")
print(f"Posledni prvek seznamu: {numbers[-1]}")
# Slovniky a mnoziny

student = {
    "jmeno": "Petr",
    "vek": 25,
    "predmety": ["Matematika", "Fyzika", "Informatika"]
}

student ["vek"] = 25
student ["jmeno"] = "Petr"
student ["predmety"] = ["Matematika", "Fyzika", "Informatika"]
print ("Student: ",student)

data = [3,3,3,4,5,6,7,8,9,9,9,10]
unique_data = set(data)
print(f"Unikatni data: {unique_data}")

for i in range(1, 11):
    if i % 3 == 0:        # cislo je delitelne 3
        print("Fizz")
    elif i % 5 == 0:      # cislo je delitelne 5
        print("Buzz")
    else:
        print(i)

def vypocet_obvodu_obdelniku(delka, sirka):
    return 2 * (delka + sirka)

delka = 5
sirka = 3
print(f"Obvod obdelniku s delkou {delka} a sirkou {sirka} je: {vypocet_obvodu_obdelniku(delka, sirka)}")

def vypocet_obsahu_telesa(delka, sirka=None):
    if sirka is None:
        sirka = delka
    return 2 * (delka + sirka)

delka = 5
sirka = 3
print(f"Obsah telesa s delkou {delka} a sirkou {sirka} je: {vypocet_obsahu_telesa(delka, sirka)}")

# odmocnina
odmocnina = math.sqrt(256)
print(f"Odmocnina z 256 je: {odmocnina}")

print(dir(math))