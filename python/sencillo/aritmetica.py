class Aritmetica:
    """
    Comentarios para las clases :O 
    Clase Aritmetica para realizar las operacnes de sumar,restar,etc    
    """

    def __init__(self,operandoA,operandoB):
        self.operandoA=operandoA
        self.operandoB=operandoB

    def sumar(self):
        return self.operandoA+self.operandoB

    def restar(self):
        return self.operandoA-self.operandoB

    def dividir(self):
        return self.operandoA/self.operandoB

    def multiplicar(self):
        return self.operandoA*self.operandoB

    

aritmetica1 = Aritmetica(5,3)
print(aritmetica1.sumar())
print(f'SUMA: {aritmetica1.sumar()}')
print('RESTA: ',aritmetica1.restar())
print(f'DIVISION: {aritmetica1.dividir():.2f}')
# lo que sta despuesd los parentesis indica los puntos flotantes que se mostrarán
print(f'MULTIPLICAR: {aritmetica1.multiplicar()}')
