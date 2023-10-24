#include<math.h>
#include<stdio.h>


int main(){

    double i;
    scanf("%le", &i);

    double menor;
    double maior;

    menor = i/log(i);
    maior = 1.25506 * (i/log(i));
    printf("%.1f %.1f", menor ,maior);
    
}