from .item import Item

class Comanda:
    def __init__(self, mesa):
        if mesa <= 0:
            raise ValueError("número da mesa deve ser positivo")
        self.mesa = mesa
        self._itens = [] # composição: tem uma lista
        
def adicionar_item(self, item):
    if not isinstance(item, Item):
        raise TypeError("só é possível adicionar um Item")
    self._itens.append(item)

@property
def subtotal(self):
    return sum(i.preco for i in self._itens)