import pytest

from calculadora import sumar
def test_vacio_da_cero():
    assert sumar("") == 0