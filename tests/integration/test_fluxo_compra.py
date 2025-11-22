import pytest
from src.loja_online.loja import Loja
from src.loja_online.carrinho import Carrinho
from src.loja_online.pagamento import Pagamento
from src.loja_online.entrega import Entrega


class TestFluxoCompra:
    def test_fluxo_completo_compra_simples(self):
        """Testa o fluxo completo de uma compra simples"""
        # Setup da loja
        loja = Loja()

        # Cadastrar cliente
        cliente = loja.cadastrar_cliente(1, "João Silva", "joao@email.com")
        assert cliente is not None

        # Cadastrar produtos
        produto1 = loja.cadastrar_produto(1, "Notebook", 3000.0)
        produto1.definir_estoque(10)

        produto2 = loja.cadastrar_produto(2, "Mouse", 50.0)
        produto2.definir_estoque(20)

        # Criar carrinho e adicionar produtos
        carrinho = Carrinho()
        carrinho.adicionar_produto(produto1, 1)
        carrinho.adicionar_produto(produto2, 2)

        total_carrinho = carrinho.calcular_total()
        assert total_carrinho == 3100.0

        # Criar pedido
        pedido = loja.criar_pedido(cliente.id)
        for item in carrinho.itens:
            pedido.adicionar_item(item["produto"], item["quantidade"])

        assert pedido.total == 3100.0

        # Confirmar pedido
        pedido.confirmar_pedido()
        assert pedido.status == "confirmado"

        # Processar pagamento
        pagamento = Pagamento(1, pedido.total, "cartao")
        resultado_pagamento = pagamento.processar_pagamento()
        assert resultado_pagamento is True
        assert pagamento.status == "processado"

        # Criar entrega
        entrega = Entrega(1, pedido.id, "Rua A, 123")
        entrega.iniciar_entrega()
        assert entrega.status == "em_transito"

        entrega.confirmar_entrega()
        assert entrega.status == "entregue"

        # Adicionar ao histórico do cliente
        cliente.adicionar_compra(pedido)
        assert len(cliente.historico) == 1
        assert cliente.obter_total_gasto() == 3100.0

    def test_fluxo_compra_multiplos_produtos(self):
        """Testa compra com múltiplos produtos e quantidades"""
        loja = Loja()

        # Cadastrar cliente
        cliente = loja.cadastrar_cliente(1, "Maria Santos", "maria@email.com")

        # Cadastrar vários produtos
        produto1 = loja.cadastrar_produto(1, "Notebook", 3000.0)
        produto1.definir_estoque(5)

        produto2 = loja.cadastrar_produto(2, "Mouse", 50.0)
        produto2.definir_estoque(10)

        produto3 = loja.cadastrar_produto(3, "Teclado", 150.0)
        produto3.definir_estoque(10)

        produto4 = loja.cadastrar_produto(4, "Monitor", 1000.0)
        produto4.definir_estoque(3)

        # Criar carrinho com múltiplos produtos
        carrinho = Carrinho()
        carrinho.adicionar_produto(produto1, 2)
        carrinho.adicionar_produto(produto2, 3)
        carrinho.adicionar_produto(produto3, 1)
        carrinho.adicionar_produto(produto4, 1)

        total_esperado = (3000.0 * 2) + (50.0 * 3) + (150.0 * 1) + (1000.0 * 1)
        assert carrinho.calcular_total() == total_esperado

        # Criar e processar pedido
        pedido = loja.criar_pedido(cliente.id)
        for item in carrinho.itens:
            pedido.adicionar_item(item["produto"], item["quantidade"])

        assert pedido.total == total_esperado
        pedido.confirmar_pedido()

        # Adicionar ao histórico
        cliente.adicionar_compra(pedido)
        assert cliente.obter_total_gasto() == total_esperado

    def test_fluxo_verificacao_estoque(self):
        """Testa a verificação de estoque durante o processo de compra"""
        loja = Loja()

        # Cadastrar produto com estoque limitado
        produto = loja.cadastrar_produto(1, "Notebook", 3000.0)
        produto.definir_estoque(2)

        # Verificar disponibilidade
        disponivel = loja.estoque.verificar_disponibilidade(1, 2)
        assert disponivel is True

        disponivel = loja.estoque.verificar_disponibilidade(1, 3)
        assert disponivel is False

        # Simular compra reduzindo estoque
        assert produto.reduzir_estoque(2) is True
        assert produto.estoque == 0

        # Verificar que não há mais estoque
        disponivel = loja.estoque.verificar_disponibilidade(1, 1)
        assert disponivel is False

    def test_fluxo_cancelamento_pedido(self):
        """Testa o fluxo de cancelamento de um pedido"""
        loja = Loja()

        cliente = loja.cadastrar_cliente(1, "Pedro Alves", "pedro@email.com")
        produto = loja.cadastrar_produto(1, "Notebook", 3000.0)
        produto.definir_estoque(5)

        # Criar pedido
        pedido = loja.criar_pedido(cliente.id)
        pedido.adicionar_item(produto, 1)
        pedido.confirmar_pedido()

        # Criar pagamento
        pagamento = Pagamento(1, pedido.total, "cartao")

        # Cancelar pedido e pagamento
        pedido.cancelar_pedido()
        pagamento.cancelar_pagamento()

        assert pedido.status == "cancelado"
        assert pagamento.status == "cancelado"

    def test_fluxo_multiplas_compras_cliente(self):
        """Testa múltiplas compras do mesmo cliente"""
        loja = Loja()

        cliente = loja.cadastrar_cliente(1, "Ana Costa", "ana@email.com")

        # Primeira compra
        produto1 = loja.cadastrar_produto(1, "Mouse", 50.0)
        produto1.definir_estoque(10)

        pedido1 = loja.criar_pedido(cliente.id)
        pedido1.adicionar_item(produto1, 2)
        pedido1.confirmar_pedido()
        cliente.adicionar_compra(pedido1)

        # Segunda compra
        produto2 = loja.cadastrar_produto(2, "Teclado", 150.0)
        produto2.definir_estoque(10)

        pedido2 = loja.criar_pedido(cliente.id)
        pedido2.adicionar_item(produto2, 1)
        pedido2.confirmar_pedido()
        cliente.adicionar_compra(pedido2)

        # Terceira compra
        produto3 = loja.cadastrar_produto(3, "Monitor", 1000.0)
        produto3.definir_estoque(5)

        pedido3 = loja.criar_pedido(cliente.id)
        pedido3.adicionar_item(produto3, 1)
        pedido3.confirmar_pedido()
        cliente.adicionar_compra(pedido3)

        # Verificar histórico e total gasto
        assert len(cliente.historico) == 3
        total_esperado = (50.0 * 2) + (150.0 * 1) + (1000.0 * 1)
        assert cliente.obter_total_gasto() == total_esperado

    def test_fluxo_remocao_item_carrinho(self):
        """Testa a remoção de itens do carrinho antes de finalizar compra"""
        loja = Loja()

        produto1 = loja.cadastrar_produto(1, "Notebook", 3000.0)
        produto2 = loja.cadastrar_produto(2, "Mouse", 50.0)
        produto3 = loja.cadastrar_produto(3, "Teclado", 150.0)

        carrinho = Carrinho()
        carrinho.adicionar_produto(produto1, 1)
        carrinho.adicionar_produto(produto2, 2)
        carrinho.adicionar_produto(produto3, 1)

        assert len(carrinho.itens) == 3

        # Remover um item
        carrinho.remover_produto(2)
        assert len(carrinho.itens) == 2

        # Calcular novo total
        total_esperado = (3000.0 * 1) + (150.0 * 1)
        assert carrinho.calcular_total() == total_esperado

    def test_fluxo_rastreamento_entrega(self):
        """Testa o rastreamento completo de uma entrega"""
        loja = Loja()

        cliente = loja.cadastrar_cliente(1, "Carlos Lima", "carlos@email.com")
        produto = loja.cadastrar_produto(1, "Notebook", 3000.0)

        pedido = loja.criar_pedido(cliente.id)
        pedido.adicionar_item(produto, 1)
        pedido.confirmar_pedido()

        # Criar entrega e acompanhar status
        entrega = Entrega(1, pedido.id, "Rua B, 456")

        assert entrega.obter_status() == "preparando"

        entrega.iniciar_entrega()
        assert entrega.obter_status() == "em_transito"

        entrega.confirmar_entrega()
        assert entrega.obter_status() == "entregue"

    def test_integracao_estoque_produtos(self):
        """Testa a integração entre estoque e produtos"""
        loja = Loja()

        # Adicionar múltiplos produtos
        for i in range(1, 6):
            produto = loja.cadastrar_produto(i, f"Produto {i}", float(i * 100))
            produto.definir_estoque(i * 2)

        # Verificar produtos no estoque
        produtos = loja.estoque.listar_produtos()
        assert len(produtos) == 5

        # Verificar disponibilidade de cada produto
        for i in range(1, 6):
            disponivel = loja.estoque.verificar_disponibilidade(i, i)
            assert disponivel is True
