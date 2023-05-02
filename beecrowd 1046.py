inicio, fim = map(int, input().split())

if fim <= inicio:
    fim = fim + 24

tempo = fim - inicio
print(f"O JOGO DUROU {tempo} HORA(S)")