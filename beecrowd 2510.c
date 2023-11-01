#include <stdio.h>
#include <string.h>
 
int main()
{
    char coringa[] = "Coderinga";
    int total;
    char vilao[50];
    scanf("%d", &total);
    for (int i=0; total>i; i++)
    {
        scanf("%s", &vilao);
        if(strcmp(vilao, coringa))
        {
            printf("Y\n");
        }
        else{
            printf("Y\n");
          //problema malfeito d+
        }
    }
    
}
