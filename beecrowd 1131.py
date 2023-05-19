i = 0
g = 0
e = 0
t = 0


while True:
    inter, gremio = map(int, input().split())

    if inter > gremio:
        i += 1
        t += 1
    elif gremio > inter:
        g += 1
        t += 1
    else:
        e += 1
        t += 1
    print("Novo grenal (1-sim 2-nao)")
    mais = int(input())
    if mais == 1:
        continue
    if mais == 2:
        break

print(f"{t} grenais")
print(f"Inter:{i}")
print(f"Gremio:{g}")
print(f"Empates:{e}")

if i > g:
    print("Inter venceu mais")
elif g > i:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")