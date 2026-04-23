class Funcionario:
    def __init__(self, nome: str, matricula: str):
        if not nome:
            raise ValueError("O nome do funcionário não pode ser vazio.")
        self.nome = nome
        if not matricula:
            raise ValueError("A matrícula do funcionário não pode ser vazia.")
        self.matricula = matricula

    def calcular_pagamento(self):
        print(f"Calculando pagamento para o funcionário {self.nome} (Matrícula: {self.matricula})")

class Assalariado(Funcionario):
    def __init__(self, nome: str, matricula: str, salario: float):
        super().__init__(nome, matricula)
        if salario <= 0:
            raise ValueError("O salário tem que ser > 0")
        self.salario = salario

    def calcular_pagamento(self):
        super().calcular_pagamento()
        return self.salario

class Horista(Funcionario):
    def __init__(self, nome: str, matricula: str, horas_trabalhadas: int, valor_hora: float):
        super().__init__(nome, matricula)
        if horas_trabalhadas < 0:
            raise ValueError("As horas trabalhadas têm que ser > 0.")
        self.horas_trabalhadas = horas_trabalhadas
        if valor_hora < 0:
            raise ValueError("O valor da hora tem que ser >= 0.")
        self.valor_hora = valor_hora

    def calcular_pagamento(self):
        super().calcular_pagamento()
        return self.horas_trabalhadas * self.valor_hora

class Comissionado(Funcionario):
    def __init__(self, salario_base: float, total_vendas: float, percentual_comissao: float, nome: str, matricula: str):
        super().__init__(nome, matricula)
        if salario_base <= 0:
            raise ValueError("O salário base tem que ser > 0.")
        self.salario_base = salario_base
        if total_vendas < 0:
            raise ValueError("O total de vendas tem que ser > 0.")
        self.total_vendas = total_vendas
        if percentual_comissao < 0 or percentual_comissao > 100:
            raise ValueError("O percentual de comissão deve estar entre 0 e 100.")
        self.percentual_comissao = percentual_comissao
    def calcular_pagamento(self):
        super().calcular_pagamento()
        return self.salario_base + (self.total_vendas * self.percentual_comissao / 100)

class Financeiro:
    def __init__(self, nome_departamento: str):
        if not nome_departamento:
            raise ValueError("O nome do departamento financeiro não pode ser vazio.")
        self.nome_departamento = nome_departamento

    def processar_pagamento(self, funcionario: Funcionario):
        funcionario.calcular_pagamento()
        print(
            f"Departamento {self.nome_departamento} processou o pagamento de {funcionario.nome}"
            f"Matrícula: {funcionario.matricula} | Valor: R$ {funcionario.calcular_pagamento}"
        )

        ##Falta validar a´porcentagem da comissao