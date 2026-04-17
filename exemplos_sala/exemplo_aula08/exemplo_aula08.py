from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def calcular_custo(self):
        pass

class TransporteRodoviario(Transporte):
    def __init__(self, distancia: float, custo_por_km: float):
        self.distancia = distancia
        self.custo_por_km = custo_por_km
    
    def calcular_custo(self):
        return self.distancia * self.custo_por_km
    
class TransporteAereo(Transporte):
    def __init__(self, peso: float, custo_por_kg: float, taxa_fixa: float):
        self.peso = peso
        self.custo_por_kg = custo_por_kg
        self.taxa_fixa = taxa_fixa
    
    def calcular_custo(self):
        return (self.peso * self.custo_por_kg) + self.taxa_fixa
    
class NaoInstancia(Transporte):
    def hello_world():
        print("Hello, World!")