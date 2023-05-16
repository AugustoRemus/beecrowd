a = True
while a == True:
    n = int(input())
    if n == 0:
        break
    else:
        lista = []
        b = map(int, input().split())
        lista = [int(digito) for digito in b]
        p = sum(lista)
        print(f"Mary won {n - p} times and John won {p} times")
        continue
