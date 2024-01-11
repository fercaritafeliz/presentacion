from figuraGeometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self, alto,color):
#       super().__init__(ancho)
        FiguraGeometrica.__init__(self,alto,alto)
        Color.__init__(self,color)

    def calcularArea(self):
        return self.alto*self.ancho