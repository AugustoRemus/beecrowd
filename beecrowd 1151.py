n = int(input())

lista = []

a = 0
b = 1
print(a, end=' ')

for i in range(n - 2):
    printar = a + b
    print(printar, end=' ')
    b = a
    a = printar

print(b + printar)