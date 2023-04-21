t = int(input())

hora = 0
minuto = 0

if t >= 3600:
    hora = t // 3600
    t = t % 3600

if t >= 60:
    minuto = t // 60
    t = t % 60

print(f"{hora}:{minuto}:{t}")

