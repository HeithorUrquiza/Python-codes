class Fracao:
    
    # método construtor
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        if denominador == 0:
            raise TypeError("O denominador não pode ser 0")
        else: 
            self.denominador = denominador  
            
    def somar(self, fracao):
        if self.denominador == fracao.denominador:
            num = self.numerador + fracao.numerador
            den = self.denominador
            return Fracao(num, den)
        num = self.numerador * fracao.numerador + fracao.denominador * self.denominador
        den = self.denominador * fracao.denominador
        return Fracao(num, den)
               
    def subtrair(self, fracao):
        return self.somar(fracao.negar())
        
    def multiplicar(self, fracao):
        numer = self.numerador * fracao.numerador
        denom = self.denominador * fracao.denominador
        return Fracao(numer, denom)
    
    def dividir(self, fracao):
        return self.multiplicar(fracao.inverter())
        
    def inverter(self):
        return Fracao(self.denominador, self.numerador)
    
    def negar(self):
        return Fracao(-self.numerador, self.denominador)
    
    # método para string
    def __str__(self):
        representation = "{}/{}".format(self.numerador, self.denominador)
        return representation
    
    # método par representação
    def __repr__(self):
        representation = "Fracao({}, {})".format(self.numerador, self.denominador)
        return representation
    
    # sobrecarg operador soma
    def __add__(self, fracao):
        return self.somar(fracao)
    
    # sobrecarg operador subtração
    def __sub__(self, fracao):
        return self.subtrair(fracao)
    
    # sobrecarg operador multiplicação
    def __mul__(self, fracao):
        return self.multiplicar(fracao)
    
# Teste
if __name__ == '__main__':
    a = Fracao(2, 3)
    b = Fracao(1, 3)
    print(a * b)