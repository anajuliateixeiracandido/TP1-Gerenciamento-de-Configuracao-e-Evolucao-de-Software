import random
import string

class Utilitarios:
    @staticmethod
    def gerar_id():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    @staticmethod
    def formatar_preco(valor):
        return f"R$ {valor:.2f}"

    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email

    @staticmethod
    def calcular_desconto(valor, porcentagem):
        return valor * (porcentagem / 100)

    @staticmethod
    def aplicar_desconto(valor, porcentagem):
        desconto = Utilitarios.calcular_desconto(valor, porcentagem)
        return valor - desconto