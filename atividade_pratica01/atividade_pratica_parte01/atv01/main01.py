from atividade_appoo01 import Bolo

def main():
    bolo1 = Bolo("Bolo de Chocolate", "Morango", "Pão de Ló", True)
    print(bolo1.cobertura)

    bolo2 = Bolo("Bolo de Morango", "Chocolate", "Pão de Ló", False)
    print(bolo2.cobertura)

    bolo3 = Bolo("Bolo de Chocolate 2", "Morango", "Pão de Ló", False)
    print(bolo3.cobertura)

    bolo1.cobertura = False
    print(bolo1.cobertura)

main()