soma = 0
while True:
    aa, bb = map(int, input().split())
    soma = 0
    if aa > 0 and bb > 0:
        if aa < bb:
            a = bb
            b = aa
        else:
            a = aa
            b = bb

        for i in range(b, a + 1):
            soma += i
            print(i, end=" ")
        print(f"Sum={soma}")

    else:
        break