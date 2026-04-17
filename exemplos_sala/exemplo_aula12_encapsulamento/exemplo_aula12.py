class Funcionario:
    def __init__(self, nome: str, salario: float, id: str):
        self.nome = nome
        self._salario = salario
        self.__id = id

    ##falta terminar este exercicio