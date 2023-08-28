import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws Exception
    {
        
        float numero1;
        float numero2;
        float printar;
        
        
        Scanner leitor = new Scanner(System.in);
        numero1 = leitor.nextFloat();
        numero2 = leitor.nextFloat();

        printar = numero1 / numero2;

       
        System.out.printf("%.2f", printar);
        
    }
}
