jmeno = input("Zadej jmeno: ")
prijmeni = input("Zadej prijmeni: ")
vek = int(input("Zadej vek: "))
zaliba = input("Zadej zalibu: ")
print(f"Jmenuji se {jmeno} {prijmeni}, je mi {vek} let a moje zaliba je {zaliba}.")

# Pevně zadané přihlašovací údaje (v reálné aplikaci by byly v databázi)
SPRAVNE_JMENO = "admin"
SPRAVNE_HESLO = "heslo123"

# Počítadlo pokusů
pokusy = 3

while pokusy > 0:
    uzivatelske_jmeno = input ("Zadej uživatelské jméno: ")
    heslo = input("Zadej heslo: ")

    if uzivatelske_jmeno == SPRAVNE_JMENO and heslo == SPRAVNE_HESLO:
        print("Přihlášení úspěšné!")
        break
