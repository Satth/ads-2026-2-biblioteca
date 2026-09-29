from decimal import Decimal


PRODUTO = {
    "biscoito": Decimal("35.00"),
    "salgadinho": Decimal("25.00"),
    "refrigerante": Decimal("15.00"),
    "gelatina": Decimal("40.00"),
}


class Comanda:
    def __init__(self, itens, produto=PRODUTO, minimo_desconto=3):
        self.itens = itens
        self.produto = produto
        self.minimo_desconto = minimo_desconto

    @property
    def minimo_desconto(self):
        return self._minimo_desconto

    @minimo_desconto.setter
    def minimo_desconto(self, valor):
        if valor < 1:
            raise ValueError("O minimo de itens para desconto deve ser pelo menos 1.")
        self._minimo_desconto = valor

    def itens_validos(self):
        """Devolve apenas os itens que existem no catalogo."""
        validos = []
        for item in self.itens:
            if item in self.produto:
                validos.append(item)
        return validos

    def subtotal(self):
        """Soma o preco dos itens validos."""
        total = Decimal("0.00")
        for item in self.itens_validos():
            total += self.produto[item]
        return total

    def desconto(self):
        """Calcula 10 por cento de desconto a partir do minimo de itens validos."""
        if len(self.itens_validos()) >= self.minimo_desconto:
            return self.subtotal() * Decimal("0.10")
        return Decimal("0.00")

    def fechar(self):
        """Devolve subtotal, desconto e total."""
        sub = self.subtotal()
        desc = self.desconto()
        return {"subtotal": sub, "desconto": desc, "total": sub - desc}
