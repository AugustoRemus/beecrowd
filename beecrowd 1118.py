import sys

total = 0
numeros = 0
media = 0
fazer = True
cu = True
while True:
    while fazer == True:
        a = float(input())
        if a > 10 or a < 0:
            print("nota invalida")
            continue

        else:
            total += a
            numeros += 1
            break

    if numeros > 1:
        media = total / numeros
        total = 0
        numeros = 0
        print(f"media = {media:.2f}")

        cu = True

        while cu == True:
            print("novo calculo (1-sim 2-nao)")
            no = float(input())
            if no == 1:
                cu = False
                break

            if no == 2:
                sys. exit()

            else:
                continue


            break