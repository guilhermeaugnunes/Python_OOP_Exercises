from exemplo_aula08 import *

def main():
    transporte1 = TransporteRodoviario(800, 5)
    print(f"Valor rodoviario: {transporte1.calcular_custo()}")

    transporte2 = TransporteAereo(70, 9, 45)
    print(f"Valor aereo: {transporte2.calcular_custo()}")

    transporteErro = NaoInstancia()

main()