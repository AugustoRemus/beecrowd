a = int(input())
b = int(input())


if a > b:
    maior = a
    menor = b
elif b > a:
    maior = b
    menor = a

printar = 0

while maior > (menor + 1):
    maior = maior - 1
    c = maior % 2
    if c == 0:
        continue
    else:
        printar = printar + maior

print(printar)