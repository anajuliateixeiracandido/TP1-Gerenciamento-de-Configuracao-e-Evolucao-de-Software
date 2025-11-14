from loja import Loja
from utilitarios import Utilitarios

def main():
    loja = Loja()
    
    produto1 = loja.cadastrar_produto(1, "Notebook", 2500.00)
    produto1.definir_estoque(10)
    
    produto2 = loja.cadastrar_produto(2, "Mouse", 50.00)
    produto2.definir_estoque(20)
    
    cliente1 = loja.cadastrar_cliente(1, "João Silva", "joao@email.com")
    
    pedido = loja.criar_pedido(1)
    pedido.adicionar_item(produto1, 1)
    pedido.adicionar_item(produto2, 2)
    
    print(f"Total do pedido: {Utilitarios.formatar_preco(pedido.total)}")
    
    pedido.confirmar_pedido()
    cliente1.adicionar_compra(pedido)
    
    print(f"Total gasto pelo cliente: {Utilitarios.formatar_preco(cliente1.obter_total_gasto())}")

if __name__ == "__main__":
    main()