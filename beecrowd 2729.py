n = int(input())
for i in range(n):
    aa = []
    aa = input().split()
    lenm = len(aa)
    for d in range(lenm):
        teste = aa[0]
        aa.pop(0)
        if teste in aa:
            aa.remove(teste)
        aa.append(teste)

    aa = sorted(aa, reverse=False, key=str)
    dd = len(aa)
    for c in range(dd - 1):
        print(aa[c], end=" ")
    print(aa[dd - 1])