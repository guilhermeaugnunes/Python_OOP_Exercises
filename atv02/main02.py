from atividade_appoo02 import FazBolo
def main():
    Bolo1 = FazBolo("Pão de Ló", "Morango", "Chocolate")
    Bolo1.assar("media", 90)

    print("\n")

    Bolo2 = FazBolo("Chocolate", "Doce de Leite", "Brigadeiro")
    Bolo2.assar("alta", 10)

    print("\n")

    Bolo3 = FazBolo("Baunilha", "Creme", "Frutas")
    Bolo3.assar("baixa", -45)

main()