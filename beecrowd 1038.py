a, b = map(float, input().split())

preco = 0

if a == 1:
    preco = preco + 4

if a == 2:
    preco = preco + 4.50



if a == 3:
    preco = preco + 5



if a == 4:
    preco = preco + 2



if a == 5:
    preco = preco + 1.50


preco = preco * b

print(f"Total: R$ {preco:.2f}")


