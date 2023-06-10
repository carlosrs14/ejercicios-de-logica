import java.util.Scanner;

public class pitagoras {

    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int A, B;
            double H;
            System.out.print("Ingrese el catedo A: ");
            A=scan.nextInt();
            System.out.print("Ingrese el catedo B: ");
            B=scan.nextInt();
            H = Math.sqrt(A*A + B*B);
            System.out.println("La hipotenusa es: "+H);
        }
    }   
}