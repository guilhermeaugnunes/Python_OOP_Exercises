from pratica03_01 import *
def main():
    evento = "Show de Rock"
    valor = 100.00
    taxa = 0.5 * valor

    ingresso = Ingresso(evento, valor)
    ingresso_vip = IngressoVIP(evento, valor, taxa)
    ingresso_meia = IngressoMeiaEntrada(evento, valor)

    ingressos = [ingresso, ingresso_vip, ingresso_meia]

    for i  in ingressos:
        print(f"Tipo de ingresso: {type(i).__name__}")
        print(f"Evento: {i.evento}")
        print(f"Valor do ingresso: R$ {i.calcular_valor():.2f} \n")
        
if __name__ == "__main__":
    main()