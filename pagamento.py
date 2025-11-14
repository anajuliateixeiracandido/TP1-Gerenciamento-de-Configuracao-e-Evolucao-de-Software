class Pagamento:
    def __init__(self, id, valor, metodo):
        self.id = id
        self.valor = valor
        self.metodo = metodo
        self.status = "pendente"

    def processar_pagamento(self):
        self.status = "processado"
        return True

    def cancelar_pagamento(self):
        self.status = "cancelado"

    def verificar_status(self):
        return self.status