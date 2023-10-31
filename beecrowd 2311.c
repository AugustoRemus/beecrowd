#include <stdio.h>
#include <string.h>



int main()
{
    int total;
    char competidores[50];
    float notas;
    float a,b,c,d,e,f,g;
    float dificuldade;

    scanf("%d", &total);
    

    for(int i = 0; i<total; i++)
    {

        scanf("%s", &competidores);
        

        scanf("%f", &dificuldade);
        scanf("%f %f %f %f %f %f %f",&a,&b,&c,&d,&e,&f,&g);
        float vetor[]= {a,b,c,d,e,f,g};
        float maior , menor = a;
        for(int d = 0; d<7;d++)
        {
            if(vetor[d] > maior)
                maior = vetor[d];
           
            else if(vetor[d] < menor)
                menor = vetor[d];

        }

        float nota = a+b+c+d+e+f+g;
        nota = nota - menor - maior;
        nota = nota * dificuldade;
        notas = nota;

        printf("%s %.2f\n", competidores, notas);


    }
   
   
}
