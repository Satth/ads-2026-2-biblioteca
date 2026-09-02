from functools import reduce

VENDAS = [
    {"produto": "Teclado", "valor": 150.00, "categoria": "Periferico"},
    {"produto": "Mouse", "valor": 80.00, "categoria": "Periferico"},
    {"produto": "Monitor", "valor": 900.00, "categoria": "Tela"},
    {"produto": "Cabo HDMI","valor": 35.00, "categoria": "Acessorio"},
    {"produto": "Headset", "valor": 250.00, "categoria": "Periferico"},
    {"produto": "Suporte", "valor": 120.00, "categoria": "Acessorio"},
]

IMPOSTO = 0.10
VALOR_MINIMO = 100.00

def acima_do_minimo(venda):
    """Diz se a venda entra no relatorio"""
    return venda["valor"] > VALOR_MINIMO

def aplicar_imposto(venda):
    """Devolve uma nova venda com o valor líquido
    Não altera a venda recebida. Essa é a diferenla entre uma função e uma que modifica no lugar.
    """
    return {**venda, "valor": venda["valor"] * (1 - IMPOSTO)}

def agrupar_pr_categoria(acumulado, venda):
    """Soma a venda no total da sua categoria."""
    cat = venda["categoria"]
    return {**acumulado, cat: acumulado.get(cat, 0) + venda["valor"]}

def relatorio(vendas):
    """Total liquido por categoria, apenas de vendas acima do minimo."""
    relevantes = filter(acima_do_minimo, vendas)
    liquidas = map(aplicar_imposto, relevantes)
    return reduce(agrupar_pr_categoria, liquidas, {})

if __name__ == "__main__":
    for categoria, total in relatorio(VENDAS).items():
         print(f"{categoria:12} R$ {total:8.2f}")