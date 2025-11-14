from cliente import Cliente
from produto import Produto
from pedido import Pedido
from carrinho import Carrinho
from estoque import Estoque
from pagamento import Pagamento
from entrega import Entrega

class Loja:
    def __init__(self):
        self.clientes = {}
        self.produtos = {}
        self.pedidos = {}
        self.estoque = Estoque()

    def cadastrar_cliente(self, id, nome, email):
        cliente = Cliente(id, nome, email)
        self.clientes[id] = cliente
        return cliente

    def cadastrar_produto(self, id, nome, preco):
        produto = Produto(id, nome, preco)
        self.produtos[id] = produto
        self.estoque.adicionar_produto(produto)
        return produto

    def criar_pedido(self, cliente_id):
        pedido_id = len(self.pedidos) + 1
        pedido = Pedido(pedido_id, cliente_id)
        self.pedidos[pedido_id] = pedido
        return pedido

    def buscar_cliente(self, cliente_id):
        return self.clientes.get(cliente_id)

    def buscar_produto(self, produto_id):
        return self.produtos.get(produto_id)