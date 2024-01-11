public class Personas{
    String nombre;
    int edad;
    String dni;

    public Personas(String nombre, int edad){
        this.nombre = nombre;
        this.edad = edad;
    }

    public Personas(String dni){
        this.dni = dni;
    }
    
    public void correr(){
    System.out.println("se llama "+nombre+" y tiene "+edad);
    }
  
    public void correr(int km){
    System.out.println("corrio"+km);
    }
}