#ABC = Abstrac Base Class

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto):
        # if 0<ancho<10:
        if self._validar_valor(ancho):
            self.ancho=ancho
            print(f'valor erroneo:{ancho}')
        else:
            self.ancho=0
        # if 0<alto<10:
        if self._validar_valor(alto):
            self._alto=alto
        else:
            self.alto=0
            print(f'valor erroneo:{alto}')

    @property # este decorador se usa para acceder indirectamente a la variable 
    def alto(self):
        print('Lamando metodo get nombre')
        return self._alto
    
    #Si no se agrega el set entonces se dice que es variable de solo lectura 
    @alto.setter
    def alto(self,alto):
        print('Lamando metodo set nombre')
        self._alto=alto

    @property # este decorador se usa para acceder indirectamente a la variable 
    def ancho(self):
        print('Lamando metodo get nombre')
        return self._ancho
    
    #Si no se agrega el set entonces se dice que es variable de solo lectura 
    @ancho.setter
    def ancho(self,ancho):
        print('Lamando metodo set nombre')
        self._ancho=ancho


    @abstractmethod
    def calcularArea(self):
        pass

    def __str__(self):
        return f'Figura Geometrica: [Altura: {self._alto}],[Ancho: {self._ancho}] {super().__str__()}'


    def _validar_valor(self,valor):
        return True if 0< valor <10 else False