import java.time.LocalDate;
import java.util.Scanner;

public class edad {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int d_actual, m_actual, a_actual, d_nac, m_nac, a_nac, edad=0;
            LocalDate hoy = LocalDate.now();

            System.out.print("Ingrese el dia: ");
            d_nac = scan.nextInt();
            System.out.print("Ingrese el mes: ");
            m_nac = scan.nextInt();
            System.out.print("Ingrese el año: ");
            a_nac = scan.nextInt();
            
            d_actual = hoy.getDayOfMonth();
            m_actual = hoy.getMonthValue();
            a_actual = hoy.getYear();

            if((a_nac > a_actual) || ((a_nac == a_actual) && (m_nac > m_actual)) || ((a_nac == a_actual) && (m_nac == m_actual) && (d_nac > d_actual))){
                //ingresó una fecha mayor que la de hoy
                System.out.println("La fecha ingresada es invalida");
            }else{
                edad = a_actual-a_nac;
                if((m_nac > m_actual) || ((m_nac == m_actual) && (d_nac > d_actual))){
                    //si aún no los ha cumplido
                    edad=edad-1;
                }
            }
            System.out.println("La edad de esta persona es: " + edad);
        }


    }    
}
