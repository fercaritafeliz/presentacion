public class operadorescondicionales {
    public static void main(String[] args) {
        // operadores condicionales &&and y or ||
        var a = 10;
        var valorminimo = 0;
        var valormaximo = 9;
        var resultado = valorminimo >= 0 && a <= valormaximo;

        if (resultado) {
            System.out.println("Dentro e rango");
        } else {
            System.out.println("Fuera de rango");
        }

        var vacaciones = true ;
        var diaDescanso = false;

        if(vacaciones || diaDescanso){
            System.out.println("padre puede asustir al juego del hijo");
        }
        else{
            System.out.println("El padre está ocupado");
        }

        


    }

}
