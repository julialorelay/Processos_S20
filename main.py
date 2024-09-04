from subclasses import BombaEtanol
from subclasses import BombaEtanol_litros
from subclasses import BombaGasolina
from subclasses import BombaGasolina_litros


def perguntar_valor():
    while True:
        try: 
            valor = float(input("Qual valor você deseja abastecer? "))
            return valor
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

#Exemplo de uso
bomba = BombaEtanol_litros(1000, 2.0)
litros_abastecido = perguntar_valor()
bomba.abastecer_por_litros(litros_abastecido)
print(f"Total abastecido: {bomba.obter_total_abastecido()}")
print(f"Saldo total: {bomba.obter_saldo_total()}")
 
bomba = BombaEtanol(1000, 2.0)
valor_abastecido = perguntar_valor()
bomba.abastecer_por_valor(valor_abastecido)
print(f"Total abastecido: {bomba.obter_total_abastecido()}")
print(f"Saldo total: {bomba.obter_saldo_total()}")
