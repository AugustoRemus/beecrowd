    lista = []
    total = 0
    lista = input().split()


    for i in range(len(lista)):
        lista[i] = int(lista[i])


    a = lista[0]
    lista.pop(0)

    lista.sort()

    n = lista[-1]
    izin = n

    for i in range(0, izin):
        total += a + i
    print(total)
