class Cliente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
        self.historico = []

    def adicionar_compra(self, compra):
        self.historico.append(compra)

    def obter_historico(self):
        return self.historico

    def obter_total_gasto(self):
        return sum(compra.total for compra in self.historico)