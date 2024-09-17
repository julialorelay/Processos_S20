from bomba_combustivel import BombaCombustivel

class Bombaetanol(BombaCombustivel):
    def __init__(self, quantidade, valor):
        super().__init__(quantidade, valor)
        self.total_abastecido = 0  # Inicializa o total abastecido
        self.saldo_total = 0  # Inicializa o saldo total

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor  # Calcula a quantidade de litros
        self.total_abastecido += litros  # Soma os litros abastecidos ao total
        self.saldo_total += valor  # Adiciona o valor ao saldo total
        return litros
    
    def obter_total_abastecido(self):
        return self.total_abastecido
    
    def obter_saldo_total(self):
        return self.saldo_total  

    def abastecer_por_litros(self, litros):
        self.total_abastecido += litros  # Soma os litros abastecidos ao total
        self.saldo_total += litros * self.valor  # Adiciona o valor ao saldo total
        return litros

# Testando a classe Bombaetanol
bomba = Bombaetanol(1000, 5)
resultado = bomba.abastecer_por_litros(20)
print(resultado)  
print(bomba.get_quantidade())  

resultado = bomba.abastecer_por_valor(100)
print(resultado) 
print(bomba.get_quantidade())  
