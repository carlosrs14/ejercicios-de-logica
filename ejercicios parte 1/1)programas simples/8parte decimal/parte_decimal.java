import java.util.Scanner;

public class parte_decimal {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int numeroInt;
            float numero;
            System.out.print("Ingrese un número: ");
            numero = scan.nextFloat();
            numeroInt = ((int)numero);
            numero = numero -numeroInt;
            System.out.println("La parte decimal de este número fue: " + numero);
        }
    }    
}
