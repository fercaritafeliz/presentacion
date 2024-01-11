from dispositivo_entrada import DispositivoEntrada
class Teclado(DispositivoEntrada):
    
    contador_teclados=0
    
    def __init__(self,marca,top_entrada):
        Teclado.contador_teclados+=1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca,top_entrada)

    def __str__(self):
        return f'Id: {self._id_teclado}, Marca: {self._marca}, Tipo Entrada: {self._tipo_entrada}'
    

if __name__ == '__main__':
    Teclado1=Teclado('HP','USB')
    Teclado2=Teclado('Gamer','Bluetooth')
    print(Teclado1)
    print(Teclado2)