class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = 0

    def definir_estoque(self, quantidade):
        self.estoque = quantidade

    def reduzir_estoque(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            return True
        return False

    def aumentar_estoque(self, quantidade):
        self.estoque += quantidade

    def obter_preco(self):
        return self.preco