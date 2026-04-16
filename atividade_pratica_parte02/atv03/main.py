from pratica02_03 import *
def main():
    financeiro1 = Financeiro("Departamento Financeiro")
    assalariado1 = Assalariado("João", "555", 3000.00)
    horista1 = Horista("Maria", "666", 160, 20.00)
    comissionado1 = Comissionado(2000.00, 50000.00, 10, "Carlos", "777")

    financeiro1.processar_pagamento(assalariado1)    
    financeiro1.processar_pagamento(horista1) 
    financeiro1.processar_pagamento(comissionado1) 

main()