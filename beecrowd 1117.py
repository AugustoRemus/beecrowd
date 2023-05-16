while True:
    b = float(input())
    if b >= 0 and b <= 10:
        dois = b
        break
    else:
        print("nota invalida")
        continue

while True:
    a = float(input())
    if a >= 0 and a <= 10:
        um = a
        break
    else:
        print("nota invalida")
        continue
prita = um + dois
prita = prita / 2
print(f"media = {prita:.2f}")