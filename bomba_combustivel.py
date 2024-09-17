class BombaCombustivel:
    def __init__(self, quantidade, valor):  
        self.__valor_litro = valor
        self.__quantidade = quantidade

    def get_valor(self):
        return self.__valor_litro
    
    def get_quantidade(self):
        return self.__quantidade
    
    def set_valor(self, valor):
        self.__valor_litro = valor
    
    def abastecer_por_litros(self, litros):
        if litros > self.__quantidade:
            return -1
        else:
            total = litros * self.__valor_litro
            self.__quantidade -= litros
            return total
    
    def abastecer_por_valor(self, valor):
        litros = valor / self.__valor_litro
        if litros > self.__quantidade:
            return -1
        else:
            self.__quantidade -= litros
            return litros

# Testando

bomba = BombaCombustivel(1000, 2)
resultado = bomba.abastecer_por_litros(20)
print(resultado)  # Deve imprimir 40
print(bomba.get_quantidade())  # Deve imprimir 80

bomba = BombaCombustivel(1000, 2)
resultado = bomba.abastecer_por_valor(100)
print(resultado)  # Deve imprimir 25
print(bomba.get_quantidade())  # Deve imprimir 75
