class Item:
    def __init__(self, nome, preco):
        if not nome or not nome.strip():
            raise ValueError("nome do item não pode ser vazio")
        if preco < 0:
            raise ValueError("preço não pode ser negativo")
        self.nome = nome.strip()
        self.preco = preco

    def descricao(self):
        return f"{self.nome}: R$ {self.preco}"

class Bebida(Item):
    def __init__(self, nome, preco, ml):
        super().__init__(nome, preco)
        self.ml = ml
    def descricao(self):
        base = super().descricao()
        return f"{base} ({self.ml} ml)"

class Prato(Item):
    def __init__(self, nome, preco, minutos):
        super().__init__(nome, preco)
        self.minutos = minutos
    def descricao(self):
        base = super().descricao()
        return f"{base} (~{self.minutos} min)"