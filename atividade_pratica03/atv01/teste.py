class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

teclado1 = Produto("Teclado", 150.0)
print(teclado1.nome)  # Acessa o nome do produto
print(teclado1.preco)  # Acessa o preço do produto usando name mangling