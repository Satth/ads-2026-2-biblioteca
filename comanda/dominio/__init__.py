"""Núcleo do domínio da Comanda. Não conhece banco, API nem tela."""
from .item import Item, Bebida, Prato
from .desconto import SemDesconto, Percentual, ValorFixo
from .comanda import Comanda, ComandaFechadaError