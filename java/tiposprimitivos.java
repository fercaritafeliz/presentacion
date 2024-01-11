public class tiposprimitivos {
    public static void main(String args[]) {
        /*
         * tipos primitivos enteros byte,short,int,long
         */

        byte numeroByte = 10;
        System.out.println(numeroByte);
        System.out.println("Valor minimo byte:" + Byte.MIN_VALUE);
        System.out.println("Valor minimo byte:" + Byte.MAX_VALUE);

        short numeroShort =10;
        System.out.println("numeroShort="+numeroShort);
        System.out.println("Valor minimo short:" + Short.MIN_VALUE);
        System.out.println("Valor minimo short:" + Short.MAX_VALUE);
        // si se pasa en esos valores marcará error 
        int numeroint = (int)10000000L;
        System.out.println("numeroint="+numeroint);
        System.out.println("Valor minimo int:" + Integer.MIN_VALUE);
        System.out.println("Valor minimo int:" + Integer.MAX_VALUE);
        long numerolong = 123234234L;
        System.out.println(numerolong);
        System.out.println("Valor minimo long:" + Long.MIN_VALUE);
        System.out.println("Valor minimo long:" + Long.MAX_VALUE);

        float numerofloat=(float)10.E38D;//para pasarlo a float  solo F al final
        // si convertmos mal se pierde presision y se va a infinito
        System.out.println(numerofloat);
        System.out.println("Valor minimo float:" + Float.MIN_VALUE);
        System.out.println("Valor minimo float:" + Float.MAX_VALUE);
        
        double numeroDouble = 10;
        System.out.println(numeroDouble);
        System.out.println("valor minimo tipo double"+ Double.MIN_VALUE);
        System.out.println("valor maximo tipo double"+ Double.MAX_VALUE);



    }

}
