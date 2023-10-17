def encontrar_suma_de_multiplos():
    total = 0
    for elemento in range(1000):
        if elemento % 3 == 0 or elemento % 5 == 0:
            total += elemento
    print(total)