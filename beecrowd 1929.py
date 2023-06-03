def triangulos(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        forma = True
    else:
        forma = False
    return forma

a, b, c, d = map(int, input().split())

if triangulos(a, b, c) == True:
    print("S")

elif triangulos(a, b, d) == True:
    print("S")

elif triangulos(a, c, d) == True:
    print("S")

elif triangulos(c, b, d) == True:
    print("S")

else:
    print("N")


