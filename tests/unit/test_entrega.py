import pytest
from src.loja_online.entrega import Entrega


class TestEntrega:
    def test_criar_entrega(self):
        """Testa a criação de uma entrega"""
        entrega = Entrega(1, 10, "Rua A, 123")
        assert entrega.id == 1
        assert entrega.pedido_id == 10
        assert entrega.endereco == "Rua A, 123"
        assert entrega.status == "preparando"

    def test_iniciar_entrega(self):
        """Testa o início de uma entrega"""
        entrega = Entrega(1, 10, "Rua A, 123")
        entrega.iniciar_entrega()
        assert entrega.status == "em_transito"

    def test_confirmar_entrega(self):
        """Testa a confirmação de entrega"""
        entrega = Entrega(1, 10, "Rua A, 123")
        entrega.iniciar_entrega()
        entrega.confirmar_entrega()
        assert entrega.status == "entregue"

    def test_obter_status_preparando(self):
        """Testa a obtenção do status preparando"""
        entrega = Entrega(1, 10, "Rua A, 123")
        assert entrega.obter_status() == "preparando"

    def test_obter_status_em_transito(self):
        """Testa a obtenção do status em trânsito"""
        entrega = Entrega(1, 10, "Rua A, 123")
        entrega.iniciar_entrega()
        assert entrega.obter_status() == "em_transito"

    def test_obter_status_entregue(self):
        """Testa a obtenção do status entregue"""
        entrega = Entrega(1, 10, "Rua A, 123")
        entrega.iniciar_entrega()
        entrega.confirmar_entrega()
        assert entrega.obter_status() == "entregue"

    def test_fluxo_completo_entrega(self):
        """Testa o fluxo completo de uma entrega"""
        entrega = Entrega(1, 10, "Rua A, 123")
        assert entrega.status == "preparando"

        entrega.iniciar_entrega()
        assert entrega.status == "em_transito"

        entrega.confirmar_entrega()
        assert entrega.status == "entregue"
