import java.util.Scanner;

public class que_nota_necesito {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner((System.in))) {
            int c1, c2, lab;
            double faltante;
            
            System.out.print("Ingrese la nota del primer corte: ");
            c1 = scan.nextInt();
            System.out.print("Ingrese la nota del segundo corte: ");
            c2 = scan.nextInt();
            System.out.print("Ingrese la nota del laboratorio: ");
            lab = scan.nextInt();

            faltante = 3*(60-lab*0.3)/0.7 - c1 - c2;
            System.out.println("La nota que debe sacar en el último certamen es: " + faltante);
        }
    }    
}
