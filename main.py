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
