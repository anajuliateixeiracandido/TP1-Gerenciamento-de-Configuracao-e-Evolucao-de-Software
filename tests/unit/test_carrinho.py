import pytest
from src.loja_online.carrinho import Carrinho
from src.loja_online.produto import Produto


class TestCarrinho:
    def test_criar_carrinho(self):
        """Testa a criação de um carrinho vazio"""
        carrinho = Carrinho()
        assert carrinho.itens == []

    def test_adicionar_produto(self):
        """Testa a adição de um produto ao carrinho"""
        carrinho = Carrinho()
        produto = Produto(1, "Notebook", 3000.0)

        carrinho.adicionar_produto(produto, 2)
        assert len(carrinho.itens) == 1
        assert carrinho.itens[0]["produto"] == produto
        assert carrinho.itens[0]["quantidade"] == 2

    def test_adicionar_multiplos_produtos(self):
        """Testa a adição de múltiplos produtos"""
        carrinho = Carrinho()
        produto1 = Produto(1, "Notebook", 3000.0)
        produto2 = Produto(2, "Mouse", 50.0)

        carrinho.adicionar_produto(produto1, 1)
        carrinho.adicionar_produto(produto2, 2)

        assert len(carrinho.itens) == 2

    def test_remover_produto(self):
        """Testa a remoção de um produto do carrinho"""
        carrinho = Carrinho()
        produto1 = Produto(1, "Notebook", 3000.0)
        produto2 = Produto(2, "Mouse", 50.0)

        carrinho.adicionar_produto(produto1, 1)
        carrinho.adicionar_produto(produto2, 2)
        carrinho.remover_produto(1)

        assert len(carrinho.itens) == 1
        assert carrinho.itens[0]["produto"].id == 2

    def test_calcular_total_carrinho_vazio(self):
        """Testa o cálculo do total com carrinho vazio"""
        carrinho = Carrinho()
        assert carrinho.calcular_total() == 0

    def test_calcular_total_com_produtos(self):
        """Testa o cálculo do total do carrinho"""
        carrinho = Carrinho()
        produto1 = Produto(1, "Notebook", 3000.0)
        produto2 = Produto(2, "Mouse", 50.0)

        carrinho.adicionar_produto(produto1, 2)
        carrinho.adicionar_produto(produto2, 3)

        total = carrinho.calcular_total()
        assert total == 6150.0  

    def test_limpar_carrinho(self):
        """Testa a limpeza do carrinho"""
        carrinho = Carrinho()
        produto = Produto(1, "Notebook", 3000.0)

        carrinho.adicionar_produto(produto, 1)
        carrinho.limpar_carrinho()

        assert len(carrinho.itens) == 0
