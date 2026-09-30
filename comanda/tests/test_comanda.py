import pytest

from dominio import (
    Comanda,
    ComandaFechadaError,
    Item,
    Percentual,
    SemDesconto,
    ValorFixo,
)


ITENS_AULA_6 = [("água", 6), ("prato", 32), ("sobremesa", 14)]


def comanda_com_itens(desconto=None):
    c = Comanda(mesa=5, desconto=desconto)

    for nome, preco in ITENS_AULA_6:
        c.adicionar_item(Item(nome, preco))

    return c


def test_total_sem_desconto_e_52():
    assert comanda_com_itens().total == 52


@pytest.mark.parametrize(
    "desconto, esperado",
    [
        (SemDesconto(), 52),
        (Percentual(10), 46.8),
        (ValorFixo(60), 0),
    ],
)
def test_total_com_cada_desconto(desconto, esperado):
    assert comanda_com_itens(desconto).total == pytest.approx(esperado)


def test_mesa_invalida_levanta_erro():
    with pytest.raises(ValueError):
        Comanda(mesa=0)


def test_comanda_fechada_nao_recebe_item():
    c = comanda_com_itens()

    c.fechar()

    with pytest.raises(ComandaFechadaError):
        c.adicionar_item(Item("café", 5))


def test_nao_fecha_comanda_vazia():
    with pytest.raises(ValueError):
        Comanda(mesa=1).fechar()


def test_itens_devolve_copia():
    c = comanda_com_itens()

    c.itens.append(Item("intruso", 0))  # mexe só na cópia

    assert len(c.itens) == 3


def test_so_aceita_item():
    with pytest.raises(TypeError):
        Comanda(mesa=1).adicionar_item(("tupla", 5))


def test_percentual_fora_da_faixa():
    with pytest.raises(ValueError):
        Percentual(150)
