"""Descontos trocáveis.
Polimorfismo (Aula 7): as três classes respondem ao mesmo verbo, aplicar,
sem herança entre elas (duck typing). A Comanda não precisa saber qual é qual.
"""

class SemDesconto:
    def aplicar(self, subtotal):
        return subtotal

class Percentual:
    def __init__(self, pct):
        if not 0 < pct <= 100:
            raise ValueError("Percentual deve estar entre 0 e 100")
        self.pct = pct

    def aplicar(self, subtotal):
        return subtotal * (100 - self.pct)/ 100

class ValorFixo:
    def __init__(self, valor):
        if valor < 0:
            raise ValueError("Valor do desconto não pode ser negativo")
        self.valor = valor

    def aplicar(self, subtotal):
        # invariante: o total nunca fica negativo
        return max(subtotal - self.valor, 0)