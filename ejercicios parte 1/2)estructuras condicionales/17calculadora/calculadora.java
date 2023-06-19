import java.util.Scanner;
/**
 * calculadora
 */
public class calculadora {

    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            double n1, n2, rta=0;
            String operador;
            System.out.print("Ingrese un operando: ");
            n1= scan.nextInt();
            System.out.print("Ingrese el operador: ");
            operador= scan.next();
            System.out.print("Ingrese un operando: ");
            n2= scan.nextInt();

            switch (operador) {
                case "+":
                    rta = n1+n2;
                    break;
                case "-":
                    rta = n1-n2;
                    break;
                case "*":
                    rta = n1*n2;
                    break;
                case "/":
                    if(n2==0){
                        System.out.println("No se puede dividir entre 0");
                        return;
                    }else{
                        rta = n1/n2;
                    }
                    break;
                case "**":
                    rta = Math.pow(n1, n2);
                    break;
            
                default:
                    System.out.println("Opción invalida");
                    return;
            }
            System.out.println(n1 + " " + operador + " " + n2 + " = " + rta);

        }
    }
}