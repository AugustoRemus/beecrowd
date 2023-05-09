numero = int(input())
resto = 0
while numero > 0:
    numero -= 1
    a = int(input())
    resto = a % 2
    if a == 0:
        print("NULL")
        continue
    if resto == 0:
        bbb = "EVEN"
    if a >= 0:
        aaa = "POSITIVE"
    if a < 0:
        aaa = "NEGATIVE"
    if resto != 0:
        bbb = "ODD"
    print(f"{bbb} {aaa}")
