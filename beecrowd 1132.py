a = int(input())
b = int(input())

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

soma = 0
for i in range(menor, maior + 1):
    if (i % 13) != 0:
        soma += i
print(soma)