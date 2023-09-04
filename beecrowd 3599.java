import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws Exception
    {
        
        Scanner leitor = new Scanner(System.in);
        int contador = 0;

        int numeros;
        numeros = leitor.nextInt();
        int lista[] = new int[numeros];
        
        
        while (contador < numeros)
        {
            lista[contador] = leitor.nextInt(); 
            contador++;
        }
       contador = 1;
       System.out.print(lista[0]);
        
       while (contador < numeros)
        {
            System.out.print(" " + lista[contador]);
            
            contador ++;
        }

        System.out.println();
        contador = 0;
        while (contador < numeros)
        {
           
            System.out.println(lista[contador]);
            contador ++;
        }
        

    }
}
