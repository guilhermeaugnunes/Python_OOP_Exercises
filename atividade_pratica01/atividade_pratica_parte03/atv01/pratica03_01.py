class Ingresso:
    def __init__(self, evento: str, valor):
        if valor < 0:
            raise ValueError("O valor do ingresso não pode ser negativo.")
        if not evento:
            raise ValueError("O nome do evento não pode ser vazio.")
        self.evento = evento
        self.valor = valor
    def calcular_valor(self) -> float:
        return self.valor

class IngressoVIP(Ingresso):
    def __init__(self, evento: str, valor, valor_adicional):
        super().__init__(evento, valor)
        if valor_adicional < 0:
            raise ValueError("O valor adicional do ingresso VIP não pode ser negativo.")
        self.valor_adicional = valor_adicional
    def calcular_valor(self) -> float:
        return self.valor + self.valor_adicional

class IngressoMeiaEntrada(Ingresso):
    def calcular_valor(self):
        return super().calcular_valor() / 2