from atividade_appoo03 import CarroAlugado, Locadora

def main(): 
        locadora1 = Locadora("Locadora A")
        carro1 = CarroAlugado("Modelo X", 5, 300)
        locadora1.determine_valor_aluguel(carro1)
main()