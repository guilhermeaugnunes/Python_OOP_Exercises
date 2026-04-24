from abc import ABC, abstractmethod
from pathlib import Path

class Emprestimo(ABC):
    @abstractmethod
    def registrar(self):
        pass

class EmprestimoLivro(Emprestimo):
    def __init__(self, nome_usuario: str, titulo: str):
        self.nome_usuario = nome_usuario
        self.titulo = titulo

    def registrar(self):
        ...

class EmprestimoRevista(EmprestimoLivro):
    def __init__(self, nome_usuario: str, titulo: str, edicao: int):
        super().__init__(nome_usuario, titulo)
        self.edicao = edicao
    
    def registrar(self):
        ...