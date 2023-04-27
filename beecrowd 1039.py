from sys import stdin
for line in stdin:
    ra, xa, ya, rb, xb, yb = map(int, line.split())

    esquerda_a = xa - ra
    direita_a = xa + ra

    esquerda_b = xb - rb
    direita_b = xb + rb

    cima_a = ya + ra
    baixo_a = ya - ra

    cima_b = yb + rb
    baixo_b = yb - rb

    if esquerda_b <= esquerda_a:
        print("MORTO")

    elif direita_b >= direita_a:
        print("MORTO")

    elif cima_b >= cima_a:
        print("MORTO")

    elif baixo_b <= baixo_a:
        print("MORTO")

    else:
        print("RICO")



