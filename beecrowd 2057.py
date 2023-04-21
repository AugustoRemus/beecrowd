s, v, f = map(int, input().split())

tempo = s + v + f

fazer = True

if tempo >= 24 and tempo != 0:
    tempo = tempo - 24
    fazer = False

if tempo <= 0 and fazer == True:
    tempo = tempo + 24

if tempo == 24:
    tempo = 0

print(tempo)