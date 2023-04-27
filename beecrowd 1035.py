a, b, c, d = map(int, input().split())

resto = a % 2
cd = c + d
ab = a + b


if b > c and d > a and cd > ab and c >= 0 and d >= 0 and resto == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")