#include <stdio.h>

int main()
{
    float total, s, b, a, ts, tb,ta, a1, a2 ,a3;
    scanf("%f", &total);
    
    for (int i = 0; i<total; i++)
    {
        scanf("%*s");

        scanf("%f %f %f",&a1, &a2, &a3);
        ts = ts+a1;
        tb = tb+a2;
        ta = ta+a3;
        

        scanf("%f %f %f",&a1, &a2, &a3);
        s = s+a1;
        b = b+a2;
        a = a+a3;

    }
    s= s/ts * 100;
    b= b/tb * 100;
    a = a/ta * 100;
    printf("Pontos de Saque: %.2f %%.\n", s);
    printf("Pontos de Bloqueio: %.2f %%.\n", b);
    printf("Pontos de Ataque: %.2f %%.\n", a);

   
   
}
