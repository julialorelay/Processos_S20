from bomba_combustivel import BombaCombustivel
from main import perguntar_litros, perguntar_valor 

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
    
    def perguntar_litros():
      while True:
        try:
            litros = float(input("Quantos litros você deseja abastecer? "))
            return litros
        except ValueError:
            print("Por favor, insira um valor numérico válido.")


def menu():
    print("Escolha o tipo de bomba:")
    print("1. Bomba Etanol")
    print("2. Bomba Etanol por Litros")
    print("3. Bomba Gasolina")
    print("4. Bomba Gasolina por Litros")
    print("0. Sair")

    escolha = input("Digite a opção desejada: ")
    
    if escolha == '0':
        return False

    if escolha == '1':
        bomba = BombaEtanol(1000, 2.0)
        valor = perguntar_valor()
        bomba.abastecer_por_valor(valor)
        print(f"Total abastecido: {bomba.obter_total_abastecido()}")
        print(f"Saldo total: {bomba.obter_saldo_total()}")

    elif escolha == '2':
        bomba = BombaEtanol_litros(1000, 2.0)
        litros = perguntar_litros()
        bomba.abastecer_por_litros(litros)
        print(f"Total abastecido: {bomba.obter_total_abastecido()}")
        print(f"Saldo total: {bomba.obter_saldo_total()}")

    elif escolha == '3':
        bomba = BombaGasolina(1000, 3.0)
        valor = perguntar_valor()
        bomba.abastecer_por_valor(valor)
        print(f"Total abastecido: {bomba.obter_total_abastecido()}")
        print(f"Saldo total: {bomba.obter_saldo_total()}")

    elif escolha == '4':
        bomba = BombaGasolina_litros(1000, 3.0)
        litros = perguntar_litros()
        bomba.abastecer_por_litros(litros)
        print(f"Total abastecido: {bomba.obter_total_abastecido()}")
        print(f"Saldo total: {bomba.obter_saldo_total()}")

    else:
        print("Opção inválida. Tente novamente.")

    return True

