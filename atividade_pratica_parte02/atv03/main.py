from pratica02_03 import *
def main():
    assalariado1 = Assalariado("João", "Silva", 3000.00)
    financeiro1 = Financeiro("Departamento Financeiro")

    financeiro1.processar_pagamento(assalariado1)
    
main()