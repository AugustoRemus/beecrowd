#include <stdio.h>

int main()
{
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);

    if(a + b - c == 0 || a - b -c==0 ||  a+c -b==0 ||  b+c -c ==0 ||  a-c==0 ||  a-b==0 ||  b-c==0 ||  a ==0||  b==0 ||  c ==0)
    {
        printf("S\n");
    }
    else{
        printf("N\n");
    }
}
