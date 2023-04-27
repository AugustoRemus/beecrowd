a, b, c = map(float, input().split())

if (a + b) > c and (c + a) > b and (b + c) > a:
    perimetro = a + b + c

    print(f"Perimetro = {perimetro}")

else:
    area = ((a + b) / 2) * c
    print(f"Area = {area}")