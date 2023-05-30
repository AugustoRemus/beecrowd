n = int(input())
for i in range(n):
    pessoa1, cont1, pessoa2, cont2 = map(str, input().split())
    a, b = map(int, input().split())
    resto = (a + b) % 2
    if resto == 0:
        if cont1 == "PAR":
            print(pessoa1)
        else:
            print(pessoa2)
    elif resto == 1:
        if cont1 == "IMPAR":
            print(pessoa1)
        else:
            print(pessoa2)