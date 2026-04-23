class Pedido:
    def __init__(self, tipo_cafe, quantidade):
        self.tipo_cafe = tipo_cafe
        self.quantidade = quantidade

class Cafeteira:
    def __init__ (self, modelo_maquina):
        self.modelo_maquina = modelo_maquina

    def preparar_cafe(self, pedido):
        tempo_preparo: int = 2
        if pedido.quantidade < 1:
            raise ValueError("Quantidade inválida. O pedido deve conter pelo menos 1 café.")
            return 0
        tempo_total: int = tempo_preparo * pedido.quantidade
        print(f"Preparando {pedido.quantidade} x {pedido.tipo_cafe} na máquina {self.modelo_maquina}. Tempo estimado: {tempo_total} minutos.")  
        return tempo_total