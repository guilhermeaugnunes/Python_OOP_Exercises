from abc import ABC, abstractmethod

class Jogador(ABC): 
    def __init__ (self, nome: str):
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio")
        self.__nome = nome

    @property 
    def nome(self): #getter
        return self.__nome

    @abstractmethod
    def calcula_desempenho(self):
        pass


class JogadorFutebol(Jogador):
    def __init__ (self, nome: str, gols: int, assistencias: int, partidas: int):
        super().__init__(nome)
        self.gols = gols
        self.assistencias = assistencias
        self.partidas = partidas

    @property #getter de gols
    def gols(self):
        return self._gols

    @property #getter de assist
    def assistencias(self):
        return self._assistencias

    @property #getter de partidas
    def partidas(self):
        return self._partidas

    @gols.setter
    def gols(self, valor: int):
        if valor < 0:
            raise ValueError("A quantidade de gols não pode ser negativa.")
        self._gols = valor

    @assistencias.setter
    def assistencias(self, valor: int):
        if valor < 0:
            raise ValueError("A quantidade de assistencias não pode ser negativa.")
        self._assistencias = valor

    @partidas.setter
    def partidas(self, valor: int):
        if valor < 0:
            raise ValueError("A quantidade de partidas não pode ser negativa.")
        self._partidas = valor

    def calcula_desempenho(self):
        #cada gol é 15 pontos, assitencia 4 pontos, partidas 2 pontos
        return (self._gols * 15) + (self._assistencias * 4) + (self._partidas * 2)


class JogadorBasquete(Jogador):
    def __init__ (self, nome: str, cestas: int, rebotes: int, assistencias: int):
        super().__init__(nome)
        self.cestas = cestas
        self.rebotes = rebotes
        self.assistencias = assistencias

    @property #getter de cestas
    def cestas(self):
        return self._cestas

    @property #getter de rebotes
    def rebotes(self):
        return self._rebotes

    @property #getter de assistencias
    def assistencias(self):
        return self._assistencias

    @cestas.setter
    def cestas(self, valor: int):
        if valor < 0:
            raise ValueError("A quantidade de cestas não pode ser negativa.")
        self._cestas = valor

    @rebotes.setter
    def rebotes(self, valor: int):
        if valor < 0:
            raise ValueError("A quantidade de rebotes não pode ser negativa.")
        self._rebotes = valor

    @assistencias.setter
    def assistencias(self, valor: int):
        if valor < 0:
            raise ValueError("A quantidade de assistencias não pode ser negativa.")
        self._assistencias = valor

    def calcula_desempenho(self):
        #cada cesta é 10 pontos, rebote 5 pontos, assitencia 3 pontos
        return (self._cestas * 10) + (self._rebotes * 5) + (self._assistencias * 3)


class JogadorVolei(Jogador):
    def __init__ (self, nome: str, aces: int, bloqueios: int, ataques: int):
        super().__init__(nome)
        self.aces = aces
        self.bloqueios = bloqueios
        self.ataques = ataques

    @property #getter de aces
    def aces(self):
        return self._aces

    @property #getter de bloqueios
    def bloqueios(self):
        return self._bloqueios

    @property #getter de ataques
    def ataques(self):
        return self._ataques
   
    @aces.setter
    def aces(self, valor: int):
        if valor < 0:
            raise ValueError("A quantidade de aces não pode ser negativa.")
        self._aces = valor

    @bloqueios.setter
    def bloqueios(self, valor: int):
        if valor < 0:
            raise ValueError("A quantidade de bloqueios não pode ser negativa.")
        self._bloqueios = valor

    @ataques.setter
    def ataques(self, valor: int):
        if valor < 0:
            raise ValueError("A quantidade de ataques não pode ser negativa.")
        self._ataques = valor

    def calcula_desempenho(self):
        #cada ace é 12 pontos, bloqueio 5 pontos, ataque 7 pontos
        return (self._aces * 12) + (self._bloqueios * 5) + (self._ataques * 7)


class TimeAnalise:
    def __init__(self):
        self._jogadores = []

    def adiciona_jogadores(self, jogador: Jogador):
        if not isinstance(jogador, Jogador):
            raise TyperError("É necessário um objeto do tipo Jogador")
        self._jogadores.append(jogador)
        print(f"Jogdor {jogador.nome} adicionado com sucesso")

    def exibir_estatisticas(self):
        if not self._jogadores:
            print("Não existe jogadores cadastrados")
            return

        for j in self._jogadores:
            desempenho = j.calcula_desempenho()
            print(f"Jogador {j.nome}, desempenho: {desempenho}\n")

    def melhor_desempenho(self): #idnentifica o jogador com melhor desempenho
        if not self._jogadores:
            print("Não existe jogadores cadastrados para realizar a análise")
            return
        melhor_jogador = self._jogadores[0]
        maior_pontuacao = melhor_jogador.calcula_desempenho()

        for j in self._jogadores[1:]:
            pontuacao_atual = j.calcula_desempenho()
            if pontuacao_atual > maior_pontuacao:
                maior_pontuacao = pontuacao_atual
                melhor_jogador = j
            
        print(f"Destaque: {melhor_jogador.nome} com {maior_pontuacao} pontos")


if __name__ == "__main__":
    analise = TimeAnalise()
    
    try:
        #instancias de tipos diferentes
        jogador1 = JogadorFutebol("C. Ronaldo", 30, 10, 8)
        jogador2 = JogadorBasquete("Michael Jordan", 20, 30, 15)
        jogador3 = JogadorVolei("Giba", 20, 25, 28)

        #erro
        #jogador4 = JogadorFutebol("Maradona" -40)

        analise.adiciona_jogadores(jogador1)
        analise.adiciona_jogadores(jogador2)
        analise.adiciona_jogadores(jogador3)
        #analise.adiciona_jogadores(jogador4)

    except ValueError as e:
        print(f"Erro ao cadastrar: {e}")

    print("\nEstatística dos Jogadores:\n")
    analise.exibir_estatisticas()
    analise.melhor_desempenho()