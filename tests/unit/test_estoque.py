import pytest
from src.loja_online.estoque import Estoque
from src.loja_online.produto import Produto


class TestEstoque:
    def test_criar_estoque(self):
        """Testa a criação de um estoque vazio"""
        estoque = Estoque()
        assert estoque.produtos == {}

    def test_adicionar_produto(self):
        """Testa a adição de um produto ao estoque"""
        estoque = Estoque()
        produto = Produto(1, "Notebook", 3000.0)

        estoque.adicionar_produto(produto)
        assert 1 in estoque.produtos
        assert estoque.produtos[1] == produto

    def test_remover_produto(self):
        """Testa a remoção de um produto do estoque"""
        estoque = Estoque()
        produto = Produto(1, "Notebook", 3000.0)

        estoque.adicionar_produto(produto)
        estoque.remover_produto(1)

        assert 1 not in estoque.produtos

    def test_remover_produto_inexistente(self):
        """Testa a remoção de um produto que não existe"""
        estoque = Estoque()
        estoque.remover_produto(999)  
        assert True

    def test_buscar_produto_existente(self):
        """Testa a busca de um produto existente"""
        estoque = Estoque()
        produto = Produto(1, "Notebook", 3000.0)

        estoque.adicionar_produto(produto)
        produto_encontrado = estoque.buscar_produto(1)

        assert produto_encontrado is not None
        assert produto_encontrado.id == 1

    def test_buscar_produto_inexistente(self):
        """Testa a busca de um produto inexistente"""
        estoque = Estoque()
        produto_encontrado = estoque.buscar_produto(999)
        assert produto_encontrado is None

    def test_listar_produtos(self):
        """Testa a listagem de produtos do estoque"""
        estoque = Estoque()
        produto1 = Produto(1, "Notebook", 3000.0)
        produto2 = Produto(2, "Mouse", 50.0)

        estoque.adicionar_produto(produto1)
        estoque.adicionar_produto(produto2)

        produtos = estoque.listar_produtos()
        assert len(produtos) == 2

    def test_verificar_disponibilidade_suficiente(self):
        """Testa a verificação de disponibilidade com estoque suficiente"""
        estoque = Estoque()
        produto = Produto(1, "Notebook", 3000.0)
        produto.definir_estoque(10)

        estoque.adicionar_produto(produto)
        disponivel = estoque.verificar_disponibilidade(1, 5)

        assert disponivel is True

    def test_verificar_disponibilidade_insuficiente(self):
        """Testa a verificação de disponibilidade com estoque insuficiente"""
        estoque = Estoque()
        produto = Produto(1, "Notebook", 3000.0)
        produto.definir_estoque(3)

        estoque.adicionar_produto(produto)
        disponivel = estoque.verificar_disponibilidade(1, 5)

        assert disponivel is False

    def test_verificar_disponibilidade_produto_inexistente(self):
        """Testa a verificação de disponibilidade de produto inexistente"""
        estoque = Estoque()
        disponivel = estoque.verificar_disponibilidade(999, 1)
        assert disponivel is False
