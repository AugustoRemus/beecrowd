n = int(input())
for i in range(n):
    pessoa, cu = map(str, input().split())
    if pessoa == "Thor":
        print("Y")
    else:
        print("N")
