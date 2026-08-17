import pytest

from calculadora import sumar
def test_vacio_da_cero():
    assert sumar("") == 0


def test_un_solo_numero():
    assert sumar("1") == 1