while True:
    try:
        n = int(input())
        direitos = []
        esquerdos = []
        total = 0
        for i in range(n):
            numero, pe = map(str, input().split())
            if pe == "E":
                esquerdos.append(numero)
            elif pe == "D":
                direitos.append(numero)
        #print(direitos)
        #print(esquerdos)
        #print("separou")
        for d in range(len(esquerdos)):
            if esquerdos[0] in direitos:
                total += 1
                direitos.remove(esquerdos[0])
                esquerdos.pop(0)
            else:
                esquerdos.pop(0)
        print(total)

    except EOFError:
        break