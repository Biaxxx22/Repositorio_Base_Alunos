class ItemDoPedido:
    def __init__(self, produto: str, quantidade: int, preco_unitario: float):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario  

    def calcular_subtotal(self) -> float:
        return self.quantidade * self.preco_unitario


class Pedido:
        def __init__(self, id_cliente: int):
            self.id_cliente = id_cliente
            self._itens = []  
            print(f"\nPedido criado para o cliente {self.id_cliente}.")

        def adicionar_item(self, produto: str, quantidade: int, preco_unitario: float):
            novo_item = ItemDoPedido(produto, quantidade, preco_unitario)
            self._itens.append(novo_item)  
            print(f"  Item '{produto}' adicionado ao pedido.")

        def calcular_total(self):
            total = sum(item.calcular_subtotal() for item in self._itens)
            print(f"Total do pedido: {total:.2f}")


pedido_123 = Pedido(22)
pedido_123.adicionar_item("Notebook", 1, 2000.00)
pedido_123.adicionar_item("Mouse", 2, 150.00)
pedido_123.adicionar_item("Teclado", 4, 120.00)
pedido_123.adicionar_item("Tela", 7, 6789.00)
pedido_123.calcular_total()

 
