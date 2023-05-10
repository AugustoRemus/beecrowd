a = (int(input()))
coelho = 0
rato = 0
sapo = 0
total = 0
coelhoa = 0
ratoa = 0
sapoa = 0
for i in range(1,a + 1):
    numero, bixo = input().split()
    numero = int(numero)
    total += numero
    if bixo == "C":
        coelho += numero
    elif bixo == "S":
        sapo += numero
    elif bixo == "R":
        rato += numero
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
coelhoa = (coelho / total) * 100
ratoa = (rato / total) * 100
sapoa = (sapo / total) * 100
print(f"Percentual de coelhos: {coelhoa:.2f} %")
print(f"Percentual de ratos: {ratoa:.2f} %")
print(f"Percentual de sapos: {sapoa:.2f} %")

