a, b = map(int, input().split())

if a == b:
    print(b)
elif a + a > b + b:
    print(a)
else:
    print(b)