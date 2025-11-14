class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto, quantidade):
        self.itens.append({"produto": produto, "quantidade": quantidade})

    def remover_produto(self, produto_id):
        self.itens = [item for item in self.itens if item["produto"].id != produto_id]

    def calcular_total(self):
        return sum(item["produto"].preco * item["quantidade"] for item in self.itens)

    def limpar_carrinho(self):
        self.itens = []