import random
import string

def vygenerovat_heslo():
    print("---GENERATOR HESLEl---")

    #Ošetření, aby uýivatel zadal opravdu číslo
    try:
        delka_hesla = int(input("Zadejte délku hesla: "))
    except ValueError:
        print("Zadejte prosím číslo.")
        return

    if delka_hesla < 8:
        print("Heslo musí být alespoň 8 znaků dlouhé.")
        return

    #Definice znaků, ze kterych se bude heslo skládat
male_pismena = string.ascii_lowercase
velka_pismena = string.ascii_uppercase
cisla = string.digits
specialni_znaky = string.punctuation
vsechny_znaky = male_pismena + velka_pismena + cisla + specialni_znaky

#pro jistotu zajistíme, že heslo bude obsahovat alespoň jeden znak z každé kategorie
