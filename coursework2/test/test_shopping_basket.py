import pytest
from coursework2.src.shopping_basket import Basket
from coursework2.src.shopping_basket import Item

import decimal
from decimal import Decimal
from reprlib import recursive_repr

def test_add_item(setup):
    """ Given item entered is valid, 
    When item is added to basket, 
    Then ensure item is added to the list, 
    and the new total is updated """
    b.add_item(i1, 1)
    empty=b.is_empty()
    total=b.get_total_cost()
    assert empty==False
    print(empty)
    assert total==decimal.Decimal('1.52')
def test_reset(setup):
    """As a customer, I want to check if the basket is empty, so that I can prepare for the next shopping trip."
    """
    b.add_item(i1, 1)
    empty=b.is_empty()
    assert empty==False
    b.reset()
    empty=b.is_empty()
    assert empty==True
    assert b.get_total_cost()==decimal.Decimal('1.52')*0
def test_error(setup):
    with pytest.raises(ValueError,match="Quantity must be a positive number") as excinfo:
        raise ValueError("Quantity must be a positive number")
    with pytest.raises(ValueError,match="Quantity must be a positive number") as excinfo:
        b.add_item(i1,0)
