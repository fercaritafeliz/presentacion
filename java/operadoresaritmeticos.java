public class operadoresaritmeticos {
    public static void main(String[] args) {
        int a=3, b=2;
        var resultado = a+b;
        System.out.println("resultado de la suma ="+resultado);
        resultado = a-b;
        System.out.println("resultado de la resta ="+resultado);
        resultado = a*b;
        System.out.println("resultao de la multiplicación ="+resultado);
        resultado = a/b;
        System.out.println("resultado de la división ="+resultado);

        var resultado2 = 3.0/b;
        System.out.println("resultado de la división"+resultado2);

        resultado=a%b;
        System.out.println("resultao del modulo "+resultado);

        if (a%2==0) 
            System.out.println("Es numero par");
        else
            System.out.println("Es numero impar");

    }
    
}
