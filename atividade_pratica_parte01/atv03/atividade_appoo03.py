class CarroAlugado:
    def __init__(self, modelo, quantidade_dias, quilometros_rodados):
        if quantidade_dias < 0:
            raise ValueError("A quantidade de dias não pode ser negativa.")
        if quilometros_rodados < 0: 
            raise ValueError("A quantidade de quilômetros rodados não pode ser negativa.")
        self.modelo = modelo
        self.quantidade_dias = quantidade_dias
        self.quilometros_rodados = quilometros_rodados

    def forneca_valor_aluguel(self):
        dia: int = 0
        valor_diaria: float = 120.00
        valor_km : float = 0.80
        return self.quantidade_dias * valor_diaria + self.quilometros_rodados * valor_km

class Locadora:
    def __init__(self, nome_locadora):
        self.nome_locadora = nome_locadora
        
    def determine_valor_aluguel(self, carro: CarroAlugado):
        valor_aluguel = carro.forneca_valor_aluguel()
        print(f"""O carro {carro.modelo}, alugado por dias {carro.quantidade_dias} na locadora 
        {self.nome_locadora} teve o valor total de {valor_aluguel} reais, considerando
        {carro.quantidade_dias} dias de aluguel e {carro.quilometros_rodados} km rodados.""")