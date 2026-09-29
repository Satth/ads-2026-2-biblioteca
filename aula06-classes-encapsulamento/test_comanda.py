from decimal import Decimal

import pytest

from comanda import Comanda


def test_subtotal_soma_apenas_o_que_esta_no_catalogo():
    comanda = Comanda(["biscoito", "salgadinho", "arma_de_portais"])

    assert comanda.subtotal() == Decimal("60.00")


def test_item_fora_do_catalogo_nao_conta_para_o_desconto():
    comanda = Comanda(["biscoito", "salgadinho", "arma_de_portais"])

    assert comanda.desconto() == Decimal("0.00")


def test_desconto_de_dez_por_cento_a_partir_de_tres_itens():
    comanda = Comanda(["biscoito", "salgadinho", "biscoito"])

    assert comanda.subtotal() == Decimal("95.00")
    assert comanda.desconto() == Decimal("9.50")
    assert comanda.fechar()["total"] == Decimal("85.50")


def test_comanda_vazia_nao_quebra():
    comanda = Comanda([])

    assert comanda.fechar()["total"] == Decimal("0.00")


def test_itens_validos_ignora_desconhecido():
    comanda = Comanda(["biscoito", "arma_de_portais"])

    assert comanda.itens_validos() == ["biscoito"]


def test_minimo_desconto_nao_pode_ser_menor_que_um():
    with pytest.raises(ValueError):
        Comanda([], minimo_desconto=0)
