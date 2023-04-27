a, b, c = map(int, input().split())

if a > b and a > c:
    if b < c:
        aa = a
        bb = c
        cc = b

    else:
        aa = a
        bb = b
        cc = c

elif b > c and b > a:
    if a < c:
        aa = b
        bb = c
        cc = a
    else:
        aa = b
        bb = a
        cc = c

else:
    if b > a:
        aa = c
        bb = b
        cc = a
    else:
        aa = c
        bb = a
        cc = b


print(cc)
print(bb)
print(aa)
print()
print(a)
print(b)
print(c)