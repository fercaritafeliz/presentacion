public class operadoresunarios {
    public static void main(String[] args) {
        var a = 3;
        var b = -a;
        System.out.println("a ="+a);
        System.out.println("b ="+b);

        var c = true;
        var d = !c;
        System.out.println("d ="+d);

        // incremento 
        //1.preincremento (simbolo antes de la variable)
        var e = 3;
        var f = ++e;

        System.out.println("e ="+e);
        System.out.println("f = "+f);

        var g=5;
        var h = g++;//primero se utiliza el valor y despues se incrementa
        System.out.println("g ="+g);
        System.out.println("h ="+h);
        // decremento 
        var i =2;
        var j=--i;

        System.out.println("i ="+i);
        System.out.println("j ="+j);

        //posdecremento 
        var k=4;
        var l= k--; //primero se usa el valor de la variable y qyeda pendiente decremento
        System.out.println("k ="+k);
        System.out.println("l ="+l);



    }
    
}
