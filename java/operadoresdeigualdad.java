public class operadoresdeigualdad {
    public static void main(String[] args) {
        var a = 3;
        var b = 2;
        var c = (a == b);

        System.out.println("c =" + c);

        var d = a != b;
        // parentesis opcionales
        System.out.println("d =" + d);

        var cadena = "hola";
        var cadena2 = "Adios";
        var e = cadena == cadena2;// compara referencias de objetos
        System.out.println("e =" + e);

        var f = cadena.equals(cadena2);// aquí si se ve si es igual o no :v
        System.out.println("f =" + f);// comparamos contenio de cadenas

        var g = a >= b; // mayor que > o el mayor o igual que >=
        System.out.println("g =" + g);

        if (a % 2 == 0)
            System.out.println("es par ");
        else
            System.out.println("es impar");

        var edad = 30;
        var adulto = 18;
        if (edad >= adulto) {
            System.out.println("es un adulto ");
        } else {
            System.out.println("es menor de edad");
        }

        

    }

}
