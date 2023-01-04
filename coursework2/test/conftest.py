import pytest
from coursework2.src.shopping_basket import Basket
from coursework2.src.shopping_basket import Item

import decimal


@pytest.fixture
def i1():
    i1 = Item("Warburtons", "Toastie", "800g white sliced loaf", decimal.Decimal('1.52'))
    yield i1


@pytest.fixture
def i2():
    i2 = Item("Flora", "Buttery", "Buttery spread", decimal.Decimal('0.89'))
    yield i2


@pytest.fixture
def b():
    b = Basket()
    yield b
