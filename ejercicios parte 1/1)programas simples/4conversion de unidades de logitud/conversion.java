import java.util.Scanner;

public class conversion {

    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int cm;
            double in;

            System.out.println("Ingrese una distacia en cm: ");       
            cm = scan.nextInt();
            in= cm / 2.45;
            System.out.println("Esto es equivalente a "+ in +" pulgadas");
        }
    }
}