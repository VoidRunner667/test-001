for i in range(2, 100):
    for x in range(2, i):
        print (f"Kontroluji čislo {i} děliteli {x}")
        if i % x == 0:    #modulo - zbytek po deleni
            break
    else:
        print(f"{i} ========= JE PRVOČÍSLO =========")    
