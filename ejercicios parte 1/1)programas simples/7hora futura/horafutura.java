import java.util.Scanner;

public class horafutura {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int hact, aumento, hfut;
            
            System.out.print("Ingrese la hora acutal: ");
            hact = scan.nextInt();
            System.out.print("Ingrese el aumento: ");
            aumento= scan.nextInt();
            hfut = (hact+aumento) %12;

            System.out.println("La futura será: "+hfut);
        }
        
    }    
}
