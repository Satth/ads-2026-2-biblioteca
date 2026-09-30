import pytest

from dominio.item import Bebida, Item, Prato

def test_item_valido():
    item = Item("água", 6)
    assert item.descricao() == "água: R$ 6"

def test_item_com_preco_negativo_levanta_erro():
    with pytest.raises(ValueError):
        Item("erro", -1)

def test_item_sem_nome_levanta_erro():
    with pytest.raises(ValueError):
        Item(" ", 5)

def test_bebida_herda_validacao_da_mae():
# super().__init__ garante que a regra de Item vale para Bebida
    with pytest.raises(ValueError):
        Bebida("suco", -8, 300)

def test_bebida_sobrescreve_descricao_reaproveitando_a_mae():
    assert Bebida("suco", 8, 300).descricao() == "suco: R$ 8 (300 ml)"

def test_prato_e_um_item():
    assert isinstance(Prato("feijoada", 32, 25), Item)