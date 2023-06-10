import java.util.Scanner;

public class numero_inverido {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int num;
            System.out.print("Ingrese un número: ");
            num = scan.nextInt();

            inverso(num);
        }

    }

    public static void inverso(int num){
        if(num<10){
            System.out.println(num);
        }else{
            System.out.print(num%10);
            inverso(num/10);
        }
    }    
}
