#include <stdio.h>

int main() {
char alfabeto[26];

    while((scanf("%s", alfabeto) != EOF ))
    {
    
       
        int num;
        scanf("%d", &num); 

        int valor; 

        for (int i = 0; i < num; i++) {
            scanf("%d", &valor);
            printf("%c", alfabeto[valor- 1]); 
        }
        printf("\n");

        
       
        
    }


}
