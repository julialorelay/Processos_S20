class BombaCombustivel:
    def __init__(self, quantidade, valor):  
        self.__valor_litro = valor
        self.__quantidade = quantidade
        
        if BombaCombustivel:
            quantidade > 100
            return(-1)
        else:
             return self.__valor

        

    def get_valor (self):
        return self.__valor
    
    def get_quantidade (self):
        return self.__quantidade
    
    def abastecer_por_litros(self, litros):
        # valor_litro = preco do comb
        total = litros * self.__valor_litro
        return total
    
    def abastecer_por_valor(self, valor):
        self.total_abastecido += valor / 3  # Soma o valor abastecido ao total
        self.saldo_total += valor  # Adiciona o valor ao saldo total
        return valor

# Testing

bomba = BombaCombustivel(100, 2)
resultado = bomba.abastecer_por_litros(500)
print(resultado)
