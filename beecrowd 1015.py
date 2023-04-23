xa, ya = map(float, input().split())
xb, yb = map(float, input().split())

resposta = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5

print(f"{resposta:.4f}")
