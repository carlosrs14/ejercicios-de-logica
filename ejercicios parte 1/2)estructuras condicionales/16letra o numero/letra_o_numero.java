import java.util.Scanner;

public class letra_o_numero {
        public static void main(String[] args) {
            try (Scanner scan = new Scanner(System.in)) {
                System.out.print("Ingrese el caracter: ");
                String car = scan.next();
                if(car.substring(0).matches("[0-9]*")){
                    System.out.println("Es número");
                }else{
                    if(car.substring(0).matches("[A-Z]*")){
                        System.out.println("Es letra mayúscula");
                    }else{
                        if(car.substring(0).matches("[a-z]*")){
                            System.out.println("Es letra minúscula");
                        }else{
                            System.out.println("No es letra ni número");
                        }
                    }
                }
            }
        }
}
