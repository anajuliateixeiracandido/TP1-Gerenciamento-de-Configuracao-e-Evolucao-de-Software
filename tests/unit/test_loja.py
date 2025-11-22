import pytest
from src.loja_online.loja import Loja
from src.loja_online.cliente import Cliente
from src.loja_online.produto import Produto


class TestLoja:
    def test_criar_loja(self):
        """Testa a criação de uma loja"""
        loja = Loja()
        assert loja.clientes == {}
        assert loja.produtos == {}
        assert loja.pedidos == {}
        assert loja.estoque is not None

    def test_cadastrar_cliente(self):
        """Testa o cadastro de um cliente"""
        loja = Loja()
        cliente = loja.cadastrar_cliente(1, "Maria Eduarda", "maria@email.com")

        assert isinstance(cliente, Cliente)
        assert cliente.id == 1
        assert 1 in loja.clientes

    def test_cadastrar_produto(self):
        """Testa o cadastro de um produto"""
        loja = Loja()
        produto = loja.cadastrar_produto(1, "Notebook", 3000.0)

        assert isinstance(produto, Produto)
        assert produto.id == 1
        assert 1 in loja.produtos

    def test_criar_pedido(self):
        """Testa a criação de um pedido"""
        loja = Loja()
        loja.cadastrar_cliente(1, "Maria Eduarda", "maria@email.com")

        pedido = loja.criar_pedido(1)
        assert pedido.cliente_id == 1
        assert pedido.id in loja.pedidos

    def test_buscar_cliente_existente(self):
        """Testa a busca de um cliente existente"""
        loja = Loja()
        loja.cadastrar_cliente(1, "Maria Eduarda", "maria@email.com")

        cliente = loja.buscar_cliente(1)
        assert cliente is not None
        assert cliente.nome == "Maria Eduarda"

    def test_buscar_cliente_inexistente(self):
        """Testa a busca de um cliente inexistente"""
        loja = Loja()
        cliente = loja.buscar_cliente(999)
        assert cliente is None

    def test_buscar_produto_existente(self):
        """Testa a busca de um produto existente"""
        loja = Loja()
        loja.cadastrar_produto(1, "Notebook", 3000.0)

        produto = loja.buscar_produto(1)
        assert produto is not None
        assert produto.nome == "Notebook"

    def test_buscar_produto_inexistente(self):
        """Testa a busca de um produto inexistente"""
        loja = Loja()
        produto = loja.buscar_produto(999)
        assert produto is None

    def test_produto_adicionado_ao_estoque(self):
        """Testa se produto cadastrado é adicionado ao estoque"""
        loja = Loja()
        produto = loja.cadastrar_produto(1, "Notebook", 3000.0)

        produto_estoque = loja.estoque.buscar_produto(1)
        assert produto_estoque is not None
        assert produto_estoque.id == 1
