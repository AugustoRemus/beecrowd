d = int(input())

cem = 0
cin = 0
vin = 0
dez = 0
cinco = 0
dois = 0
um = 0


if d >= 100:
    cem = d // 100
    d = d % 100

if d >= 50:
    cin = d // 50
    d = d % 50

if d >= 20:
    vin = d // 20
    d = d % 20

if d >= 10:
    dez = d // 10
    d = d % 10

if d >= 5:
    cinco = d // 5
    d = d % 5

if d >= 2:
    dois = d // 2
    d = d % 2

if d >= 1:
    um = d // 1
    d = d % 1


print(f"{cem} nota(s) de R$ 100,00")
print(f"{cin} nota(s) de R$ 50,00")
print(f"{vin} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")
