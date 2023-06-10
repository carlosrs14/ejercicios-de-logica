import java.util.Scanner;

public class promedio {

    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            System.out.print("Ingrese la primera nota: ");
            int n1 = scan.nextInt();
            System.out.print("Ingrese la segunda nota: ");
            int n2 = scan.nextInt();
            System.out.print("Ingrese la tercera nota: ");
            int n3 = scan.nextInt();
            System.out.print("Ingrese la cuarta nota: ");
            int n4 = scan.nextInt();
            float promedio = (float) (n1+n2+n3+n4)/4;
            System.out.println("El promedio de esta persona es: "+promedio);
        }
        
    }
}