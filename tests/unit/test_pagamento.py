import pytest
from src.loja_online.pagamento import Pagamento


class TestPagamento:
    def test_criar_pagamento(self):
        """Testa a criação de um pagamento"""
        pagamento = Pagamento(1, 100.0, "cartao")
        assert pagamento.id == 1
        assert pagamento.valor == 100.0
        assert pagamento.metodo == "cartao"
        assert pagamento.status == "pendente"

    def test_processar_pagamento(self):
        """Testa o processamento de um pagamento"""
        pagamento = Pagamento(1, 100.0, "cartao")
        resultado = pagamento.processar_pagamento()

        assert resultado is True
        assert pagamento.status == "processado"

    def test_cancelar_pagamento(self):
        """Testa o cancelamento de um pagamento"""
        pagamento = Pagamento(1, 100.0, "cartao")
        pagamento.cancelar_pagamento()
        assert pagamento.status == "cancelado"

    def test_verificar_status_pendente(self):
        """Testa a verificação do status pendente"""
        pagamento = Pagamento(1, 100.0, "cartao")
        assert pagamento.verificar_status() == "pendente"

    def test_verificar_status_processado(self):
        """Testa a verificação do status processado"""
        pagamento = Pagamento(1, 100.0, "cartao")
        pagamento.processar_pagamento()
        assert pagamento.verificar_status() == "processado"

    def test_pagamento_diversos_metodos(self):
        """Testa criação de pagamentos com diferentes métodos"""
        pagamento_cartao = Pagamento(1, 100.0, "cartao")
        pagamento_boleto = Pagamento(2, 200.0, "boleto")
        pagamento_pix = Pagamento(3, 300.0, "pix")

        assert pagamento_cartao.metodo == "cartao"
        assert pagamento_boleto.metodo == "boleto"
        assert pagamento_pix.metodo == "pix"
