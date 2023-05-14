n = int(input())
for i in range(n):
    a = int(input())
    d = 1
    soma = 0
    while d < a:
        if a % d == 0:
            soma += d
        d += 1
    if a == soma:
        print(f"{a} eh perfeito")
    else:
        print(f"{a} nao eh perfeito")