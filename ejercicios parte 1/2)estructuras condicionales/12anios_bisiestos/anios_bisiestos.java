import java.util.Scanner;

public class anios_bisiestos {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int anio;
            System.out.print("Ingrese el año: ");
            anio = scan.nextInt();
            if(anio%4==0){
                System.out.println("Es un año bisiesto");
            }else{
                System.out.println("No es un año bisiesto");
            }
        }
    }    
}
