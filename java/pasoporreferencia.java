import clases.Personacurso;

public class pasoporreferencia {
    public static void main(String[] args) {
        Personacurso persona1 = new Personacurso();
        persona1.nombre = "Fer";
        System.out.println("persona1 nombre:" + persona1.nombre);
        persona1 = cambiaValor(persona1);
        System.out.println("persona1 nombre:" + persona1.nombre);
    }
    
    public static Personacurso cambiaValor(Personacurso persona){
        persona.nombre="Karla";
        return persona;
    }
}
