def scitani(a, b):
    """Funkce pro sčítání dvou čísel."""
    return a + b

soucet = scitani(5, 3)
print("Součet je:", soucet)

soucet2 = scitani(b=10, a=15)
print("Součet je:", soucet2)

def deleni(a, b):
    if b == 0:
        return "Nelze dělit nulou!"
    else:
        return a / b
print("Dělení je:", deleni(10, 2))