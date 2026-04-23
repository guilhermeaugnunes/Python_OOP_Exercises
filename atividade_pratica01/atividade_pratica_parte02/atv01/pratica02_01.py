class Veiculo:
    def __init__(self, marca: str, modelo: str, ano_fabricacao: int):
        if not marca.strip():
            raise TypeError ("A marca não pode ser vazia.")
        self.marca = marca

        if not modelo.strip():
            raise TypeError ("O modelo não pode ser vazio.")
        self.modelo = modelo

        if ano_fabricacao not in range (1886, 2025):
            raise TypeError ("Digite um ano válido")
        self.ano_fabricacao = ano_fabricacao

    def exibir_info(self):
        print(f"Veículo: {self.marca} {self.modelo} — Ano: {self.ano_fabricacao}")
    
class Carro(Veiculo):
    def __init__ (self, marca: str, modelo: str, ano_fabricacao: int, numero_portas: int):
        super().__init__(marca, modelo, ano_fabricacao)
        if numero_portas not in [2, 4]:
            raise ValueError ("A quantidade de portas deve ser 2 ou 4")
        self.numero_portas = numero_portas
    
    def exibir_info(self):
        super().exibir_info()
        print(f"Número de portas: {self.numero_portas}")
    
class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano_fabricacao: int, cilindrada: int):
        super().__init__(marca, modelo, ano_fabricacao)
        if cilindrada <= 0:
            raise ValueError ("A cilindrada deve ser maior que 0")
        self.cilindrada = cilindrada
    
    def exibir_info(self):
        super().exibir_info()
        print(f"Cilindrada: {self.cilindrada}")

class Caminhao(Veiculo):
    def __init__(self, marca: str, modelo: str, ano_fabricacao: int, capacidade_carga_toneladas: int):
        super().__init__(marca, modelo, ano_fabricacao)
        if capacidade_carga_toneladas <= 0:
            raise ValueError ("A capacidade de carga deve ser maior que 0")
        self.capacidade_carga_toneladas = capacidade_carga_toneladas

    def exibir_info(self):
        super().exibir_info()
        print(f"Capacidade de carga: {self.capacidade_carga_toneladas} toneladas")