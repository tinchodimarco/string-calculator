import pytest

from calculadora import sumar
def test_vacio_da_cero():
    assert sumar("") == 0


def test_un_solo_numero():
    assert sumar("1") == 1

def test_dos_numeros_separados_por_coma():
    assert sumar("1,2") == 3

def test_varios_numeros_separados_por_coma():
    assert sumar("1,2,3,5,8,13") == 32