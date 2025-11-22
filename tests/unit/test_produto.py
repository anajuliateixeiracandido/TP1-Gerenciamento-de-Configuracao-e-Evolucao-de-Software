import pytest
from src.loja_online.produto import Produto


class TestProduto:
    def test_criar_produto(self):
        """Testa a criação de um produto"""
        produto = Produto(1, "Notebook", 3000.0)
        assert produto.id == 1
        assert produto.nome == "Notebook"
        assert produto.preco == 3000.0
        assert produto.estoque == 0

    def test_definir_estoque(self):
        """Testa a definição do estoque"""
        produto = Produto(1, "Notebook", 3000.0)
        produto.definir_estoque(10)
        assert produto.estoque == 10

    def test_reduzir_estoque_com_sucesso(self):
        """Testa a redução do estoque quando há quantidade suficiente"""
        produto = Produto(1, "Notebook", 3000.0)
        produto.definir_estoque(10)

        resultado = produto.reduzir_estoque(5)
        assert resultado is True
        assert produto.estoque == 5

    def test_reduzir_estoque_quantidade_insuficiente(self):
        """Testa a redução do estoque quando não há quantidade suficiente"""
        produto = Produto(1, "Notebook", 3000.0)
        produto.definir_estoque(3)

        resultado = produto.reduzir_estoque(5)
        assert resultado is False
        assert produto.estoque == 3

    def test_reduzir_estoque_zerado(self):
        """Testa a redução de todo o estoque"""
        produto = Produto(1, "Notebook", 3000.0)
        produto.definir_estoque(5)

        resultado = produto.reduzir_estoque(5)
        assert resultado is True
        assert produto.estoque == 0

    def test_aumentar_estoque(self):
        """Testa o aumento do estoque"""
        produto = Produto(1, "Notebook", 3000.0)
        produto.definir_estoque(10)
        produto.aumentar_estoque(5)
        assert produto.estoque == 15

    def test_obter_preco(self):
        """Testa a obtenção do preço do produto"""
        produto = Produto(1, "Notebook", 3000.0)
        assert produto.obter_preco() == 3000.0
