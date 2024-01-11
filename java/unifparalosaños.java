import java.util.Scanner;

public class unifparalosaños {
    public static void main(String[] args) {
        Scanner mes2 = new Scanner(System.in);
        String mes3 = mes2.nextLine();
        int  mes = Integer.parseInt(mes3);
        var estacion="Estacion desconocida";
        if(mes==1||mes==2||mes==12){
            estacion = "Invierno";
        }
        else if(mes==3||mes==4||mes==5){
            estacion = "Primavera";            
        }
        else if (mes==6||mes==7||mes==8){
            estacion="Verano";
        }
        else if(mes==9||mes==10||mes==11){
            estacion="Otonio";
        }
        System.out.println("Estación del mes :"+estacion);
        
    }
    
}
