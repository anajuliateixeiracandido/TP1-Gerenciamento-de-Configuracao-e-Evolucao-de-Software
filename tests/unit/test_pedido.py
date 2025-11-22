import pytest
from src.loja_online.pedido import Pedido
from src.loja_online.produto import Produto


class TestPedido:
    def test_criar_pedido(self):
        """Testa a criação de um pedido"""
        pedido = Pedido(1, 100)
        assert pedido.id == 1
        assert pedido.cliente_id == 100
        assert pedido.itens == []
        assert pedido.total == 0
        assert pedido.status == "pendente"

    def test_adicionar_item(self):
        """Testa a adição de um item ao pedido"""
        pedido = Pedido(1, 100)
        produto = Produto(1, "Notebook", 3000.0)

        pedido.adicionar_item(produto, 2)
        assert len(pedido.itens) == 1
        assert pedido.itens[0]["produto"] == produto
        assert pedido.itens[0]["quantidade"] == 2

    def test_calcular_total(self):
        """Testa o cálculo do total do pedido"""
        pedido = Pedido(1, 100)
        produto1 = Produto(1, "Notebook", 3000.0)
        produto2 = Produto(2, "Mouse", 50.0)

        pedido.adicionar_item(produto1, 1)
        pedido.adicionar_item(produto2, 2)

        assert pedido.total == 3100.0  

    def test_confirmar_pedido(self):
        """Testa a confirmação de um pedido"""
        pedido = Pedido(1, 100)
        pedido.confirmar_pedido()
        assert pedido.status == "confirmado"

    def test_cancelar_pedido(self):
        """Testa o cancelamento de um pedido"""
        pedido = Pedido(1, 100)
        pedido.cancelar_pedido()
        assert pedido.status == "cancelado"

    def test_pedido_com_multiplos_itens(self):
        """Testa pedido com múltiplos itens"""
        pedido = Pedido(1, 100)
        produto1 = Produto(1, "Notebook", 3000.0)
        produto2 = Produto(2, "Mouse", 50.0)
        produto3 = Produto(3, "Teclado", 150.0)

        pedido.adicionar_item(produto1, 1)
        pedido.adicionar_item(produto2, 2)
        pedido.adicionar_item(produto3, 1)

        assert len(pedido.itens) == 3
        assert pedido.total == 3250.0
