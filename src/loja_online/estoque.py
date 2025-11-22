from .produto import Produto


class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        self.produtos[produto.id] = produto

    def remover_produto(self, produto_id):
        if produto_id in self.produtos:
            del self.produtos[produto_id]

    def buscar_produto(self, produto_id):
        return self.produtos.get(produto_id)

    def listar_produtos(self):
        return list(self.produtos.values())

    def verificar_disponibilidade(self, produto_id, quantidade):
        produto = self.buscar_produto(produto_id)
        if produto is None:
            return False
        return produto.estoque >= quantidade
