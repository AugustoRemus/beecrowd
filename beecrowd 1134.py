alcol = 0
gasosa = 0
disel = 0
while True:
    a = int(input())

    if a == 4:
        break
    if a == 1:
        alcol += 1
    if a == 2:
        gasosa += 1
    if a == 3:
        disel += 1
    else:
        continue
print("MUITO OBRIGADO")
print(f"Alcool: {alcol}")
print(f"Gasolina: {gasosa}")
print(f"Diesel: {disel}")