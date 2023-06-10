import java.util.Scanner;

public class saludo{
    public static void main(String args[]){
        try (Scanner scan = new Scanner(System.in)) {
            String nombre;
            System.out.print("Ingrese un nombre: ");
            nombre = scan.nextLine();
            System.out.println("Hola "+nombre);
        }
    }
}