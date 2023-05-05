a = float(input())

if a <= 2000:
    print("Isento")

elif a <= 3000:
    pagar = a - 2000.00
    pagar = pagar * 0.08
    print(f"R$ {pagar:.2f}")

elif a <= 4500:
    pagar = a - 3000
    pagar = pagar * 0.18
    pagar = pagar + 80
    print(f"R$ {pagar:.2f}")

else:
    pagar = a - 4500
    pagar = pagar * 0.28
    pagar = pagar + 80 + 270
    print(f"R$ {pagar:.2f}")