#include <stdio.h>
#include <string.h>

int main()
{
    char bin[101];

    scanf("%s", bin);

    int len = strlen(bin);
    int total = 0;

    for(int i=0;len>i;i++)
    {
        if(bin[i]=='1')
        {
            total++;
        }
        
    }

    if (total==0 || total%2==0)
    {
        bin[len] = '0';
    }
    else
    {
        bin[len] = '1';
    }

    printf("%s", bin);
}