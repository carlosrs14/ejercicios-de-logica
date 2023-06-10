import java.util.Scanner;

public class circulo{
    public static void main(String args[]){
        try (Scanner scan = new Scanner(System.in)) {
            int radio;
            double perimetro, area;
            System.out.print("Ingrese el radio: ");
            radio = scan.nextInt();

            area =  Math.PI * radio * radio;
            perimetro =  2 * Math.PI * radio;
            System.out.println("El perimetro es: "+perimetro);
            System.out.println("El area es: "+area);
        }
    }
}