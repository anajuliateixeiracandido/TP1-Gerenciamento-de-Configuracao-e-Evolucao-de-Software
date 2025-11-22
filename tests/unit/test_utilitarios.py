import pytest
from src.loja_online.utilitarios import Utilitarios


class TestUtilitarios:

    def test_formatar_preco(self):
        """Testa a formatação de preço"""
        preco_formatado = Utilitarios.formatar_preco(1000.50)
        assert preco_formatado == "R$ 1000.50"

    def test_formatar_preco_inteiro(self):
        """Testa a formatação de preço inteiro"""
        preco_formatado = Utilitarios.formatar_preco(100)
        assert preco_formatado == "R$ 100.00"

    def test_validar_email_valido(self):
        """Testa a validação de um email válido"""
        assert Utilitarios.validar_email("maria@email.com") is True
        assert Utilitarios.validar_email("teste@dominio.com.br") is True

    def test_validar_email_invalido(self):
        """Testa a validação de emails inválidos"""
        assert Utilitarios.validar_email("emailsemarroba.com") is False
        assert Utilitarios.validar_email("email@semponto") is False
        assert Utilitarios.validar_email("invalido") is False

    def test_calcular_desconto(self):
        """Testa o cálculo de desconto"""
        desconto = Utilitarios.calcular_desconto(1000, 10)
        assert desconto == 100.0

    def test_calcular_desconto_zero(self):
        """Testa o cálculo de desconto zero"""
        desconto = Utilitarios.calcular_desconto(1000, 0)
        assert desconto == 0.0

    def test_aplicar_desconto(self):
        """Testa a aplicação de desconto"""
        valor_final = Utilitarios.aplicar_desconto(1000, 20)
        assert valor_final == 800.0

    def test_aplicar_desconto_completo(self):
        """Testa a aplicação de 100% de desconto"""
        valor_final = Utilitarios.aplicar_desconto(500, 100)
        assert valor_final == 0.0
