import javax.swing.plaf.synth.SynthOptionPaneUI;

public class sentenisdecontrolif {
    public static void main(String[] args) {
        var condicion = true ;




        if (condicion){
            System.out.println("condicion verdadera");
        }
        else{
            System.out.println("condicion falsa");
        }
        //si se tiene mas de una linea obligatorio usar llaves

        var numero =7;
        var numeroTexto = "numero desconocido";

        if(numero ==1){
            numeroTexto = "Numero uno";
        }
        else if(numero ==2){
            numeroTexto ="Numero dos";
        }
        else if(numero ==4){
            numeroTexto = "Numero cuatro";
        }
        else{
            System.out.println("numero no enconrado ");
        }
        System.out.println("numero Texto ="+numeroTexto);


        
    }

}
