a = int(input())
b = int(input())
c = 0

if b > a:
    c = b
    a = b
    a = c

for i in range(b + 1, a + 1):
    ca = i % 5
    if ca == 2 or ca == 3:
        print(i)