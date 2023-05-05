a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

soma = 0
total = 0

if a >= 0:
    soma = soma + a
    total = total + 1

if b >= 0:
    soma = soma + b
    total = total + 1

if c >= 0:
    soma = soma + c
    total = total + 1

if d >= 0:
    soma = soma + d
    total = total + 1

if e >= 0:
    soma = soma + e
    total = total + 1

if f >= 0:
    soma = soma + f
    total = total + 1


printar = (soma / total)

print(f"{total:.0f} valores positivos")
print(f"{printar:.1f}")