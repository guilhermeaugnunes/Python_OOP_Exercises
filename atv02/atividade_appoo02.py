class FazBolo():
    def __init__(self, massa, recheio, cobertura):
        self.massa = massa
        self.recheio = recheio
        self.cobertura = cobertura
    
    def assar(self, temperatura, tempo):
        if temperatura not in ["alta", "media", "baixa"]:
            print("Temperatura inválida. Por favor, escolha entre 'alta', 'media' ou 'baixa'.")
            return
        if tempo <= 0 or tempo > 90:
            print("Tempo inválido. Por favor, insira um tempo positivo e menor ou igual a 90.")
            return
        else:
            self.temperatura = temperatura
            self.tempo = tempo
            
        print(
            f" Você está querendo assar o bolo de massa com recheio de {self.recheio} e cobertura de {self.cobertura} no fogo temperatura por "
            f"{tempo} minutos“, sendo {tempo} e {temperatura} inseridos pelo usuário"
        )
        
        if temperatura == "alta":
            print("Para o fogo alto, o bolo assa em 10 minutos. Antes fica cru e depois ele queima.")

        elif temperatura == "media":                   
            print("Para o fogo médio, o bolo assa em 30 minutos. Antes fica cru e depois ele queima.")

        elif temperatura == "baixa":
            print("Para o fogo baixo, o bolo assa em 45 minutos. Antes fica cru e depois ele queima.")