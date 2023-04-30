fod, day1 = map(str, input().split())
day1 = int(day1)

hora1, f, min1, a, seg1 = map(str, input().split())
hora1 = int(hora1)
min1 = int(min1)
seg1 = int(seg1)

fod2, day2 = map(str, input().split())
day2 = int(day2)

hora2, fa, min2, aa, seg2 = map(str, input().split())
hora2 = int(hora2)
min2 = int(min2)
seg2 = int(seg2)

segundo = seg2 - seg1
minuto = min2 - min1

hora = hora2 - hora1

if day2 == day1:
    dia = 0
elif day1 + 1 == day2:
    dia = 1
else:
    dia = day2 - day1

if segundo <= 60:
    minuto = minuto + segundo // 60
    segundo = segundo % 60

if minuto <= 60:
    hora = hora + minuto // 60
    minuto = minuto % 60

if hora <= 24:
    dia = dia + hora // 24
    hora = hora % 24

print(f"{dia} dia(s)")
print(f"{hora} hora(s)")
print(f"{minuto} minuto(s)")
print(f"{segundo} segundo(s)")