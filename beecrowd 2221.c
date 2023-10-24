#include<math.h>
#include<stdio.h>


int main(){

    double d;
    scanf("%le", &d);

    for(int i =0; i<d; i++)
    {
        int bonus;
        scanf("%d", &bonus);

        int atk1, def1, lvl1, dano1;
        int atk2, def2, lvl2, dano2;

        scanf("%d %d %d", &atk1, &def1, &lvl1);
        if(lvl1 % 2==0)
        {
            dano1 = ((atk1 + def1)/2) + bonus;
        }
        else{
            dano1 = ((atk1 + def1)/2);
        }

        scanf("%d %d %d", &atk2, &def2, &lvl2);
        if(lvl2 % 2==0)
        {
           dano2 = ((atk2 + def2)/2) + bonus;
        }
        else{
            dano2 = ((atk2 + def2)/2);
        }

        if(dano1==dano2)
        {
            printf("Empate\n");
        }
        else if(dano1>dano2)
        {
            printf("Guarte");
        }
        else{
            printf("Guarte");
        }
    }
    
}