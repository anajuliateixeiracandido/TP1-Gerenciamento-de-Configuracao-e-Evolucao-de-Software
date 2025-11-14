class Pedido:
    def __init__(self, id, cliente_id):
        self.id = id
        self.cliente_id = cliente_id
        self.itens = []
        self.total = 0
        self.status = "pendente"

    def adicionar_item(self, produto, quantidade):
        item = {"produto": produto, "quantidade": quantidade}
        self.itens.append(item)
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(item["produto"].preco * item["quantidade"] for item in self.itens)

    def confirmar_pedido(self):
        self.status = "confirmado"

    def cancelar_pedido(self):
        self.status = "cancelado"