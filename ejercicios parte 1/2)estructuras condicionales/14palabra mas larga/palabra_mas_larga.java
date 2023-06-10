import java.util.Scanner;

public class palabra_mas_larga {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            String p1, p2;
            int dif;
            System.out.print("Palabra 1: ");
            p1 = scan.next();
            System.out.print("Palabra 2: ");
            p2 = scan.next();
            
            if(p1.length() == p2.length()){
                System.out.println("Las dos palabras tienen el mismo largo");
            }else if (p1.length() > p2.length()) {
                dif = p1.length()-p2.length();
                System.out.println("La palabra "+ p1 +" tiene " + dif + " letras más que " + p2);
            }else{
                dif = p2.length()-p1.length();
                System.out.println("La palabra "+ p2 +" tiene " + dif + " letras más que " + p1);
            }
        }
        
    }    
}
