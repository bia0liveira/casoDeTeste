import unittest
from ecommerce import Produto, CarrinhoDeCompras 

class TestCarrinhoDeCompras(unittest.TestCase):

    def test_calcular_subtotal(self):
        carrinho = CarrinhoDeCompras()
        produto1 = Produto("Camisa", 50.00, 2)
        produto2 = Produto("Calça", 30.00, 1)
        carrinho.adicionar_produto(produto1)
        carrinho.adicionar_produto(produto2)
        self.assertEqual(carrinho.calcular_subtotal(), 130.00)

    def test_aplicar_desconto(self):
        carrinho = CarrinhoDeCompras()
        produto = Produto("Camisa", 100.00, 1)
        carrinho.adicionar_produto(produto)
        carrinho.aplicar_desconto(10)
        total_com_desconto = carrinho.calcular_total()
        self.assertEqual(total_com_desconto, 90.00)

    def test_aplicar_imposto(self):
        carrinho = CarrinhoDeCompras()
        produto = Produto("Camisa", 100.00, 1)
        carrinho.adicionar_produto(produto)
        carrinho.aplicar_desconto(10)
        carrinho.aplicar_imposto(8)
        total_com_imposto = carrinho.calcular_total()
        self.assertEqual(total_com_imposto, 97.20)

    def test_calcular_total(self):
        carrinho = CarrinhoDeCompras()
        produto = Produto("Camisa", 50.00, 2)
        carrinho.adicionar_produto(produto)
        carrinho.aplicar_desconto(10)
        carrinho.aplicar_imposto(8)
        total = carrinho.calcular_total()
        self.assertEqual(total, 97.20)

if __name__ == "__main__":
    unittest.main()


