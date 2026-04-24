from pratica03_02 import *

def main():
    entrega_moto = EntregaMoto("A123", 4.7, 3.0)
    entrega_caminhao = EntregaCaminhao("B456", 12.0, 9.0, 40.0)
    ##entrega_erro = Entrega("C789", 5.0)

    print(f"Custo da entrega de moto: {entrega_moto.calcular_custo():.2f}")
    print(f"Custo da entrega de caminhão: {entrega_caminhao.calcular_custo():.2f}")
    
main()