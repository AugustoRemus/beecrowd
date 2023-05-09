maior = 0
for i in range(1, 101):
    a = int(input())
    if a > maior:
        maior = a
        lugar = i
print(f"{maior}\n{lugar}")