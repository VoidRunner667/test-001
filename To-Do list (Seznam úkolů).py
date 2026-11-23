import os

SOUBOR = "ukoly.txt"

# Načte uložené úkoly ze souboru při spuštění programu
def nacist_ukoly(): 
    if os.path.exists(SOUBOR):
        with open(SOUBOR, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    return []