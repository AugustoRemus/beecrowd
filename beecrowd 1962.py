n = int(input())
printa = 0
for i in range(n):
    a = int(input())
    if a > 2014:
        printa = (2014 - a) ** 2
        printa = printa ** 0.5
        print(f"{printa:.0f} A.C.")
    else:
        printa = (2014 - a) ** 2
        printa = (printa ** 0.5) + 1
        print(f"{printa:.0f} D.C.")
