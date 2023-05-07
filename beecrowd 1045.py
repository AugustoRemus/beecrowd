aa, bb, cc = map(float, input().split())

forma = True

if aa > bb and aa > cc:
    a = aa
    b = bb
    c = cc
elif bb > aa and bb > cc:
    a = bb
    b = aa
    c = cc
elif cc > aa and cc > bb:
    a = cc
    b = aa
    c = bb

else:
    a = aa
    b = bb
    c = cc

os3 = True

for i in range(1):

    if a >= b + c:
        print("NAO FORMA TRIANGULO")
        break

    if a **2 == b ** 2 + c ** 2:
        print("TRIANGULO RETANGULO")

    if a ** 2 > b ** 2 + c ** 2:
        print("TRIANGULO OBTUSANGULO")

    if a ** 2 < b ** 2 + c ** 2:
        print("TRIANGULO ACUTANGULO")


    if a == b or a == c or c == b:
        if a == b and b == c:
            print("TRIANGULO EQUILATERO")

        elif a != b or a != c or c != b:
            print("TRIANGULO ISOSCELES")

