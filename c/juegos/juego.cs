using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class juego : MonoBehaviour
{
    [Range(1, 10)] public float velocidad; //Velocidad del jugador
    Rigidbody2D rb2d;
    SpriteRenderer spRd;


    private Animator anim;
    public float fuerzaSalto;
    public LayerMask capaSuelo;
    public int contadorDeSalto=0;
    private BoxCollider2D boxCollider;
    // Start is called before the first frame update
    void Start () {

        //2. Capturo y asocio los componentes Rigidbody2D y Sprite Renderer del Jugador
        rb2d = GetComponent<Rigidbody2D>();
        spRd = GetComponent<SpriteRenderer>();
        boxCollider=GetComponent<BoxCollider2D>();

    }

    private void Awake()
    {
        anim = GetComponentInChildren<Animator>();
    }
    bool EstaEnSuelo(){
        RaycastHit2D raycastHit = Physics2D.BoxCast(boxCollider.bounds.center,new Vector2(boxCollider.bounds.size.x,boxCollider.bounds.size.y),0f,Vector2.down,0.2f,capaSuelo);
        return raycastHit.collider != null;
    }
    void ProcesarSalto(){
        if( Input.GetKeyDown( KeyCode.Space ) && (EstaEnSuelo())){
                rb2d.AddForce(Vector2.up*fuerzaSalto,ForceMode2D.Impulse);
                Debug.Log( "espacio presioado." );
        }
        if( Input.GetKeyDown( KeyCode.Space ) && (EstaEnSuelo()!=true)){
            contadorDeSalto+=1;
            if (contadorDeSalto<2){
                rb2d.AddForce(Vector2.up*fuerzaSalto,ForceMode2D.Impulse);
                Debug.Log( "espacio en el aire." );
            }
        }
        if ((contadorDeSalto>=1) && (EstaEnSuelo())){
                contadorDeSalto=0;
            }
        if( Input.GetKeyUp( KeyCode.Space )){
            Debug.Log( "espacio soltado." );
        }
    }
    void ProcesarMovimiento(){
        //3. Movimiento horizontal
        float movimientoH = Input.GetAxisRaw("Horizontal");
        rb2d.velocity = new Vector2(movimientoH * velocidad, rb2d.velocity.y);
        
        Vector2 positionJug = transform.position;
        positionJug = positionJug+new Vector2(10*movimientoH,0f);
        transform.position = positionJug;
        //4. Sentido horizontal (para girar el render del jugador)
        if (movimientoH > 0)
        {
            spRd.flipX = false;
        }
        else if (movimientoH < 0)
        {
            spRd.flipX = true;
        }
        if( Input.GetKeyDown( KeyCode.RightArrow )){
            Debug.Log( "flecha derecha presionado.");
            Debug.Log(movimientoH);
            anim.SetFloat("Horizontal",1);
        }
        if( Input.GetKeyUp( KeyCode.RightArrow )){
            Debug.Log( "flecha derecha soltada.");
            Debug.Log(movimientoH);
            anim.SetFloat("Horizontal",0);
        }
        if( Input.GetKeyDown( KeyCode.LeftArrow )){
            Debug.Log( "flecha izquierda presionado." );
            Debug.Log(movimientoH);
            anim.SetFloat("Horizontal",1);
        }
        if( Input.GetKeyUp( KeyCode.LeftArrow )){
            Debug.Log( "flecha izquierda soltada." );
            Debug.Log(movimientoH);
            anim.SetFloat("Horizontal",0);
        }
        //clic izquierdo disparar
        if (Input.GetMouseButtonDown(0))
        {
            Debug.Log("clic en mouse");
            anim.SetTrigger("Atacar");
        }
        //clic derecho ""
        if (Input.GetMouseButtonDown(1))
            Debug.Log("clic derecho en mouse.");
        //rueda del mouse ""
        if (Input.GetMouseButtonDown(2))
            Debug.Log("ruedita.");
    }

    // Update is called once per frame
    void Update()
    {
        ProcesarMovimiento();
        ProcesarSalto();
    }
}
