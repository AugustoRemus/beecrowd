a, b, c, d = map(float, input().split())

ex = float(0)

nota = ((a * 2) + (b * 3) + (c * 4) + d) / 10

print(f"Media: {nota:.1f}")

if nota >= 7:
    print("Aluno aprovado.")

elif nota < 5:
    print("Aluno reprovado.")

else:
    ex = float(input())
    print("Aluno em exame.")
    print(f"Nota do exame: {ex}")
    nota = (nota + ex) / 2
    if nota >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {nota:.1f}")
    else:
        print("Aluno reporvado.")
        print(f"Media final: {nota:.1f}")




