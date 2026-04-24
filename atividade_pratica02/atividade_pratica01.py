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
        self.prazo = 0

    def registrar(self):
        self.prazo = 7

class EmprestimoRevista(EmprestimoLivro):
    def __init__(self, nome_usuario: str, titulo: str, edicao: int):
        super().__init__(nome_usuario, titulo)
        self.edicao = edicao
        self.prazo = 0
            
    def registrar(self):
        self.prazo = 2

class Biblioteca:
    def __init__(self):
        self.__emprestimos = []
    
    def adicionar_emprestimo(self, novo):
        for existente in self.__emprestimos:
            if (existente.nome_usuario == novo.nome_usuario and
                existente.titulo == novo.titulo):
                print(f"Alerta: O usuário {novo.nome_usuario} já possui o item '{novo.titulo}'.")
                return
            
            if isinstance(novo, EmprestimoRevista) and isinstance(existente, EmprestimoRevista):
                if existente.edicao == novo.edicao:
                    print(f"Alerta: A edição {novo.edicao} da revista já está emprestada.")
                    return

        novo.registrar()
        self.__emprestimos.append(novo)
        print(f"Empréstimo registrado: {novo.nome_usuario} - {novo.titulo} (Prazo: {novo.prazo} dias)")

    def extrair_dados(self):
        linhas = []
        for emprestimo in self.__emprestimos:
            texto = f"Usuário: {emprestimo.nome_usuario}, Título: {emprestimo.titulo}, Prazo: {emprestimo.prazo} dias"
            if isinstance(emprestimo, EmprestimoRevista):
                texto += f", Edição: {emprestimo.edicao}"
            linhas.append(texto)
        return "\n".join(linhas)

    def salvar_dados(self, nome_arquivo: str):
        caminho = Path(nome_arquivo)
        conteudo = self.extrair_dados()

        caminho.write_text(conteudo, encoding ="utf-8")
        print(f"Dados salvos em {caminho.resolve()}")


if __name__ == "__main__":
    biblioteca = Biblioteca()

    try:
        e1 = EmprestimoLivro("Guilherme", "Capitães de Areia")
        e2 = EmprestimoRevista("Guilherme", "Superinteressante", 204)
        e3 = EmprestimoLivro("Guilherme", "Capitães de Areia") #erro
        e4 = EmprestimoLivro("Luiza", "Capitães de Areia")
        e5 = EmprestimoRevista("Luiza", "Superinteressante", 204) #alerta

        biblioteca.adicionar_emprestimo(e1)
        biblioteca.adicionar_emprestimo(e2)
        biblioteca.adicionar_emprestimo(e3)
        biblioteca.adicionar_emprestimo(e4)
        biblioteca.adicionar_emprestimo(e5)

    except ValueError as e:
        print(f"Alerta: {e}")

    biblioteca.salvar_dados("dados_biblioteca.txt")