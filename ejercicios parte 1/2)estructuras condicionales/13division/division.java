import java.util.Scanner;

public class division {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int dividendo, divisor;
            System.out.print("Ingrese el dividendo: ");
            dividendo = scan.nextInt(); 
            System.out.print("Ingrese el divisor: ");
            divisor = scan.nextInt();
            if(divisor==0){
                System.out.println("No se puede dividir por 0");
                return;
            }
            if(dividendo%divisor == 0){
                System.out.println("La división es exacta");          
            }else{
                System.out.println("La división NO es exacta");
            }
            System.out.println("Cociente: " + dividendo/divisor);
            System.out.println("Residuo: " + dividendo%divisor);  
        }
    }    
}
