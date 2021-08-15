import java.util.Scanner;

public class Inicio {
    public static int IdUsuario;
    public static String IdBicicleta;
    public static String ModeloBicicleta;

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite IdUsuario: ");
        IdUsuario = teclado.nextInt();

        System.out.print("Digite IdBicicleta: ");
        IdBicicleta = teclado.next();

        System.out.print("Digite Modelo Bicicleta: ");
        ModeloBicicleta = teclado.next();
    
        Prestamo per1 = new Prestamo(IdUsuario, IdBicicleta, ModeloBicicleta);

        System.out.print("El Id de la bicicleta es: " + per1.getIdBicicleta());
    
        per1.setModeloBicicleta("2023");
        teclado.close();
    }
}