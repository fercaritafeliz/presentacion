import java.util.Scanner;

public class operadoresdeprocedencia {
    public static void main(String[] args) {
        var x =5;
        var y =10;
        var z =++x + y--;

        System.out.println("x ="+x);
        System.out.println("y ="+y);
        System.out.println("z ="+z);

        var resultado = 4+5*6/3;
        System.out.println("resultado ="+resultado);

        resultado = (4+5) * 6 /3;
        System.out.println("resultado ="+resultado);
        Scanner entrada = new Scanner(System.in);
        int altov = entrada.nextInt();
        int anchov = entrada.nextInt();
        var area = altov*anchov;
        var peri = (2*altov)+(2*anchov);
        System.out.println("Area :"+area);
        System.out.println("Perimetro :"+peri);

    }

}
