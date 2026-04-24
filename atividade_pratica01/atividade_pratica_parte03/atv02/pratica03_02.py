from abc import ABC, abstractmethod

class Entrega(ABC):
	def __init__(self, codigo: str, distancia: float):
		if not codigo:
			raise ValueError("O código da entrega não pode ser vazio.")
		if distancia < 0:
			raise ValueError("A distância da entrega não pode ser negativa.")
		self.codigo = codigo
		self.distancia = distancia

	@abstractmethod
	def calcular_custo(self) -> float:
		pass

class EntregaMoto(Entrega):
	def __init__(self, codigo: str, distancia: float, valor_por_distancia: float):
		super().__init__(codigo, distancia)
		if valor_por_distancia < 0:
			raise ValueError("O valor por distância não pode ser negativo.")
		self.valor_por_distancia = valor_por_distancia

	def calcular_custo(self) -> float:
		return self.valor_por_distancia * self.distancia
	
class EntregaCaminhao(Entrega):
	def __init__(self, codigo: str, distancia: float, valor_por_distancia: float, taxa_adicional: float):
		super().__init__(codigo, distancia)
		if valor_por_distancia < 0:
			raise ValueError("O valor por distância não pode ser negativo.")
		if taxa_adicional < 0:
			raise ValueError("A taxa adicional não pode ser negativa.")
		self.valor_por_distancia = valor_por_distancia
		self.taxa_adicional = taxa_adicional

	def calcular_custo(self) -> float:
		return (self.valor_por_distancia * self.distancia) + self.taxa_adicional