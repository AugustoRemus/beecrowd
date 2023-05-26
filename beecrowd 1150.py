x = int(input())
contador = 0
total = 0

while True:
    y = int(input())
    if x >= y:
        continue
    else:
        break
while True:
    total += x
    contador += 1
    x += 1
    if total > y:
        break
print(contador)