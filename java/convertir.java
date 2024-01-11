import java.util.Scanner;

public class convertir {
    public static void main(String[] args) {
        var edad = Integer.parseInt("20");
        System.out.println(edad+1);

        var valorPI = Double.parseDouble("3.1416");
        System.out.println(valorPI);
        
        //pedir un valor
        var consola =new Scanner(System.in);
        edad = Integer.parseInt(consola.nextLine());
        System.out.println("edad: "+edad);


        var edadTexto = String.valueOf(10);
        System.out.println(edadTexto);

        var caracter = "hola".charAt(1);
        System.out.println(caracter);

        System.out.println("Proporciona un caracter:");
        caracter = consola.nextLine().charAt(0);
        System.out.println(caracter);

        

    }

}
