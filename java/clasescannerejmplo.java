import java.util.Scanner;

public class clasescannerejmplo {
    public static void main (String args[]){
        System.out.println("escribe tu nombre");
        try (Scanner consola = new Scanner(System.in)) {
            var usuario =consola.nextLine();
            System.out.println("ususario="+usuario);
            System.out.println("Escribe tu titulo");
            var titulo = consola.nextLine();
            System.out.println("Resultado:"+titulo+""+usuario);

            System.out.println("Proporciona el titulo:");
            var titu=consola.nextLine();
            System.out.println("Proporciona el autor:");
            var aut=consola.nextLine();
            System.out.println(titu+"fue escrito por "+aut);
        }




    }
    
}
