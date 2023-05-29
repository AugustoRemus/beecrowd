n = int(input())

a = ["papel", "lagarto"] # tesoura
b = ["pedra", "Spock"] # papel
c = ["lagarto", "tesoura"] # pedra
d = ["Spock", "papel"] # lagarto
e = ["tesoura", "pedra"] #spok





for i in range(n):
    s, r = map(str, input().split())
    i = i + 1
    #teste iguais
    if s == r:
        print(f"Caso #{i}: De novo!")
        continue

    #teste tesoura
    if s == "tesoura":
        if r in a:
            print(f"Caso #{i}: Bazinga!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    #teste papel
    if s == "papel":
        if r in b:
            print(f"Caso #{i}: Bazinga!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    # teste pedra
    if s == "pedra":
        if r in c:
            print(f"Caso #{i}: Bazinga!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    #teste lagarto
    if s == "lagarto":
        if r in d:
            print(f"Caso #{i}: Bazinga!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    # teste spok
    if s == "Spock":
        if r in e:
            print(f"Caso #{i}: Bazinga!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")