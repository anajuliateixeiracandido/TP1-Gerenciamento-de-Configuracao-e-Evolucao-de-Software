class Entrega:
    def __init__(self, id, pedido_id, endereco):
        self.id = id
        self.pedido_id = pedido_id
        self.endereco = endereco
        self.status = "preparando"

    def iniciar_entrega(self):
        self.status = "em_transito"

    def confirmar_entrega(self):
        self.status = "entregue"

    def obter_status(self):
        return self.status