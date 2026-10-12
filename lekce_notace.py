# generování notaci

# vytvoření seznamu čtverců čisel od 0 do 10
squares = [x**2 for x in range(10)]
print(f"Seznam čtverců: {squares}")

mocnina = []
for i in range(10):
    mocnina.append(i**2)
    print(i, i**2)

    words = ["Python", "je", "skvělý", "programovací", "jazyk"]
    upper_words = [word.upper() for word in words]
    print(f"Slova velkými písmeny: {upper_words}")
    