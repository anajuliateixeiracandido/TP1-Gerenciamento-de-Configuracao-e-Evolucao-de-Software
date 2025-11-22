import pytest
from src.loja_online.cliente import Cliente
from src.loja_online.pedido import Pedido
from src.loja_online.produto import Produto


class TestCliente:
    def test_criar_cliente(self):
        """Testa a criação de um cliente"""
        cliente = Cliente(1, "Maria Edudarda", "maria@email.com")
        assert cliente.id == 1
        assert cliente.nome == "Maria Edudarda"
        assert cliente.email == "maria@email.com"
        assert cliente.historico == []

    def test_adicionar_compra(self):
        """Testa a adição de uma compra ao histórico"""
        cliente = Cliente(1, "Maria Edudarda", "maria@email.com")
        pedido = Pedido(1, 1)
        pedido.total = 100.0

        cliente.adicionar_compra(pedido)
        assert len(cliente.historico) == 1
        assert cliente.historico[0] == pedido

    def test_adicionar_multiplas_compras(self):
        """Testa a adição de múltiplas compras"""
        cliente = Cliente(1, "Maria Edudarda", "maria@email.com")
        pedido1 = Pedido(1, 1)
        pedido1.total = 100.0
        pedido2 = Pedido(2, 1)
        pedido2.total = 200.0

        cliente.adicionar_compra(pedido1)
        cliente.adicionar_compra(pedido2)

        assert len(cliente.historico) == 2

    def test_obter_historico(self):
        """Testa a obtenção do histórico de compras"""
        cliente = Cliente(1, "Maria Edudarda", "maria@email.com")
        pedido = Pedido(1, 1)
        pedido.total = 100.0

        cliente.adicionar_compra(pedido)
        historico = cliente.obter_historico()

        assert len(historico) == 1
        assert historico[0].total == 100.0

    def test_obter_total_gasto_sem_compras(self):
        """Testa o total gasto quando não há compras"""
        cliente = Cliente(1, "Maria Edudarda", "maria@email.com")
        assert cliente.obter_total_gasto() == 0

    def test_obter_total_gasto_com_compras(self):
        """Testa o cálculo do total gasto"""
        cliente = Cliente(1, "Maria Edudarda", "maria@email.com")
        pedido1 = Pedido(1, 1)
        pedido1.total = 100.0
        pedido2 = Pedido(2, 1)
        pedido2.total = 250.0

        cliente.adicionar_compra(pedido1)
        cliente.adicionar_compra(pedido2)

        assert cliente.obter_total_gasto() == 350.0
