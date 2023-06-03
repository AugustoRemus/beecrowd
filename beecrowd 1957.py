nu = "0123456789ABCDEF"
resultado = ""
n = int(input())
if n == 0:
    print("0")

while n > 0:
    resto = n % 16
    resultado = nu[resto] + resultado
    n = n // 16
print(resultado)


