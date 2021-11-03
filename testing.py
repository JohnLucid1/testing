
#! На моей машине чтобы запустить тест нужно написать в консоли "python -m pytest -v filename.py"
from main import Calculator
thing = Calculator(100, 5)


def test_minus_num():
    assert thing.minus_num() == 95


def test_plus_num():
    assert thing.plus_num() == 105


def test_multiply_by_num():
    assert thing.multiply_by_num() == 500


def test_devide_by_num():
    assert thing.divide_by_num() != 19


def test_to_number_power():
    assert thing.to_number_power() != 90000000000


def test_get_remainder():
    assert thing.get_remainder() == 0
