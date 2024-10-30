class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
        self.desconto = 0
        self.imposto = 0
        
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def aplicar_desconto(self, percentual):
        self.desconto = percentual

    def aplicar_imposto(self, percentual):
        self.imposto = percentual

    def calcular_subtotal(self):
        subtotal = sum(produto.preco * produto.quantidade for produto in self.produtos)
        return subtotal
    
    def calcular_total(self):
        subtotal = self.calcular_subtotal()
        valor_com_desconto = subtotal - (subtotal * self.desconto / 100)
        valor_com_imposto = valor_com_desconto + (valor_com_desconto * self.imposto /  100)
        return valor_com_imposto
        