from bomba_combustivel import BombaCombustivel

class BombaGasolina(BombaCombustivel):
    def __init__(self, quantidade, valor):
        super().__init__(quantidade, valor)

    def abastecer_por_valor_com_aditivo(self, valor):
        litro = valor *