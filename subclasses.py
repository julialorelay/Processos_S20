from combustível import BombaCombustivel 

class BombaEtanol(BombaCombustivel):
    def __init__(self, quantidade, valor):
        super().__init__(quantidade, valor)
        self.total_abastecido = 0
        self.saldo_total = 0  # Inicializa o saldo total

    def abastecer_por_valor(self, valor):
        self.total_abastecido += valor / 2  # Soma o valor abastecido ao total
        self.saldo_total += valor  # Adiciona o valor ao saldo total
        return valor
    
    def obter_total_abastecido(self):
        return self.total_abastecido
    
    def obter_saldo_total(self):
        return self.saldo_total  # Retorna o saldo total

    # abastecer_por_litros

class BombaEtanol_litros(BombaCombustivel):
    def __init__(self, quantidade, litros):
        super().__init__(quantidade, litros)
        self.total_abastecido = 0
        self.saldo_total = 0  # Inicializa o saldo total
    

    def abastecer_por_litros(self, litros):
        self.total_abastecido += litros  # Soma o litros abastecido ao total
        self.saldo_total += litros * 2  # Adiciona o litros ao saldo total
        return litros
    
    def obter_total_abastecido(self):
        return self.total_abastecido
    
    def obter_saldo_total(self):
        return self.saldo_total  # Retorna o saldo total
    
class BombaGasolina(BombaCombustivel):
    def __init__(self, quantidade, valor):
        super().__init__(quantidade, valor)
        self.total_abastecido = 0
        self.saldo_total = 0  # Inicializa o saldo total

    def abastecer_por_valor(self, valor):
        self.total_abastecido += valor / 3  # Soma o valor abastecido ao total
        self.saldo_total += valor  # Adiciona o valor ao saldo total
        return valor
    
    def abastecer_por_valor_com_aditivo(self, valor):
        self.total_abastecido += valor / 3   # Soma o valor abastecido ao total
        self.saldo_total += valor  # Adiciona o valor ao saldo total
        return valor
    
    def obter_total_abastecido(self):
        return self.total_abastecido
    
    def obter_saldo_total(self):
        return self.saldo_total  # Retorna o saldo total

    # abastecer_por_litros

class BombaGasolina_litros(BombaCombustivel):
    def __init__(self, quantidade, litros):
        super().__init__(quantidade, litros)
        self.total_abastecido = 0
        self.saldo_total = 0  # Inicializa o saldo total
    

    def abastecer_por_litros(self, litros):
        self.total_abastecido += litros  # Soma o litros abastecido ao total
        self.saldo_total += litros * 3  # Adiciona o litros ao saldo total
        return litros
    
    def abastecer_por_valor_com_aditivo(self, litros):
        self.total_abastecido += litros  # Soma o litros abastecido ao total
        self.saldo_total += litros * 3 * 1,5 # Adiciona o litros ao saldo total
        return litros
    
    def obter_total_abastecido(self):
        return self.total_abastecido
    
    def obter_saldo_total(self):
        return self.saldo_total  # Retorna o saldo total
