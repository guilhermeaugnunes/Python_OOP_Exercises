from atividade_appoo04 import *

def main():
    pedido1 = Pedido("Café Expresso", 2)
    cafeteira1 = Cafeteira("Nespresso 1")
    cafeteira1.preparar_cafe(pedido1)

    pedido2 = Pedido("Café Expresso", 5)
    cafeteira2 = Cafeteira("Nespresso 2")
    cafeteira2.preparar_cafe(pedido2)

    pedido3 = Pedido("Capuccino", 4)
    cafeteira3 = Cafeteira("Nespresso")
    cafeteira3.preparar_cafe(pedido3)

main()