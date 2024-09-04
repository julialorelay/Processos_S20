class BombaCombustivel:
    def __init__(self, quantidade, valor):  
        self.__valor = valor
        self.__quantidade = quantidade


    def get_valor (self):
        return self.__valor
    
    def get_quantidade (self):
        return self.__quantidade