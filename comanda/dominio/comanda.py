"""A Comanda de uma mesa.

Composição (Aula 7): a Comanda TEM itens e TEM um desconto.
Ela não herda de list: assim, a única porta de entrada é adicionar_item.
"""
from .desconto import SemDesconto
from .item import Item


class ComandaFechadaError(Exception):
    """Levantada ao tentar mexer numa comanda já fechada."""


class Comanda:
    def __init__(self, mesa, desconto=None):
        if mesa <= 0:
            raise ValueError("número da mesa deve ser positivo")
        self.mesa = mesa
        self._itens = []  # composição: tem uma lista
        self.desconto = desconto or SemDesconto()  # composição: tem um desconto
        self._fechada = False

    @property
    def itens(self):
        # devolve uma cópia: quem está de fora lê, mas não altera
        return list(self._itens)

    @property
    def fechada(self):
        return self._fechada

    def adicionar_item(self, item):
        if self._fechada:
            raise ComandaFechadaError("comanda fechada não recebe itens")
        if not isinstance(item, Item):
            raise TypeError("só é possível adicionar um Item")
        self._itens.append(item)

    def trocar_desconto(self, desconto):
        if self._fechada:
            raise ComandaFechadaError("comanda fechada não muda de desconto")
        self.desconto = desconto

    def fechar(self):
        if not self._itens:
            raise ValueError("não é possível fechar uma comanda vazia")
        self._fechada = True

    @property
    def subtotal(self):
        return sum(i.preco for i in self._itens)

    @property
    def total(self):
        return self.desconto.aplicar(self.subtotal)