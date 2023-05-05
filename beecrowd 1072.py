repeticoes = int(input())

dentro = 0
fora = 0

a = 0

for i in range(repeticoes):
    a = int(input())

    if a >= 10 and a <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

print(f"{dentro} in")
print(f"{fora} out")