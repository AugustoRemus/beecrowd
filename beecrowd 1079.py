n = int(input())
for i in range(1, n+1):
    a, b, c = map(float, input().split())
    aa = (a * 2 + b * 3 + c * 5) / 10
    print(f"{aa:.1f}")