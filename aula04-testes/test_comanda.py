from decimal import Decimal

from comanda.dominio import fechar, itens_validos, subtotal


def test_subtotal_soma_apenas_o_que_esta_no_catalogo():
    assert subtotal(["biscoito", "salgadinho", "arma_de_portais"]) == Decimal("60.00")


def test_item_fora_do_catalogo_nao_conta_para_o_desconto():
    conta = fechar(["biscoito", "salgadinho", "arma_de_portais"])
    assert conta["desconto"] == Decimal("0.00")

def test_desconto_de_dez_por_cento_a_partir_de_tres_itens():
    conta = fechar(["biscoito", "salgadinho", "biscoito"])
    assert conta["subtotal"] == Decimal("95.00")
    assert conta["desconto"] == Decimal("9.50")
    assert conta["total"] == Decimal("85.50")

def test_comanda_vazia_nao_quebra():
    assert fechar([])["total"] == Decimal("0.00")


def test_itens_validos_ignora_desconhecido():
    assert itens_validos(["biscoito", "arma_de_portais"]) == ["biscoito"]


