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
    
    
a = Fracao(4, 5)
b = Fracao(3, 5)
nege = a.negar()
print(nege.numerador)


