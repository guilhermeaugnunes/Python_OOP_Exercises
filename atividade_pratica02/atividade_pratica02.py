from abc import ABC, abstractmethod

class Emprestimo(ABC):
    @abstractmethod
    def registrar(self):
        pass


class EmprestimoLivro(Emprestimo):
    def __init__(self, nome_usuario: str, titulo_livro: str, prazo: int):
        self.nome_usuario = nome_usuario
        self.titulo_livro = titulo_livro
        self.prazo = prazo

    def registrar(self):
        return super().registrar()

class EmprestimoRevista(EmprestimoLivro):
    def __init__(self, nome_usuario, titulo_livro, prazo, edicao: int):
        super().__init__(nome_usuario, titulo_livro, prazo)
        self.edicao = edicao
