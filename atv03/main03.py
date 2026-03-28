from atividade_appoo03 import CarroAlugado, Locadora

def main(): 
        locadora1 = Locadora("Locadora A")
        carro1 = CarroAlugado("Fusion", 5, 300)
        locadora1.determine_valor_aluguel(carro1)

        locadora2 = Locadora("Locadora B")
        carro2 = CarroAlugado("Civic", 3, 150)
        locadora2.determine_valor_aluguel(carro2)
main()