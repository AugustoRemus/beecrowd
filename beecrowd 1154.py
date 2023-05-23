total = 0
soma = 0

while True:
    a = int(input())
    if a < 0:
        break
    else:
        soma += a
        total += 1

print(f"{(soma / total):.2f}")