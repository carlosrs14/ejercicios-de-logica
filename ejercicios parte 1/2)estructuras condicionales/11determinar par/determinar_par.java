import java.util.Scanner;

public class determinar_par {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int num;

            System.out.print("Ingrese un número: ");
            num = scan.nextInt();
            if(num%2==0){
                System.out.println("Su número es par");
            }else{
                System.out.println("Su número es impar");
            }
        }
    }
}
