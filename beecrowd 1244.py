n = int(input())
for i in range(n):
    palavras = []
    palavras = input().split()
    palavras = sorted(palavras, reverse=True, key=len)
    d = len(palavras)
    for o in range(d - 1):
        print(palavras[o], end=" ")
    print(palavras[d - 1])
