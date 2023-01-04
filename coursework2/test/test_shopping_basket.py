import pytest
from coursework2.src.shopping_basket import Basket
from coursework2.src.shopping_basket import Item

import decimal
from decimal import Decimal
from reprlib import recursive_repr

def test_add_item(i1,i2,b):
    """ Given item entered is valid, 
    When item is added to basket, 
    Then ensure item is added to the list, 
    and the new total is updated """
    b.add_item(i1, 1)
    assert b.is_empty()==False
    assert b.get_total_cost()==decimal.Decimal('1.52')
def test_remove_item(i1,i2,b):
    """ Given item entered is valid, 
    When item is removed to basket, 
    Then ensure item is removed from the list, 
    and the new total is updated """
    b.update_item(i1, 10)
    b.remove_item(i1,2)
    assert b.items[i1]==10-2
    assert b.get_total_cost()==decimal.Decimal('1.52')*8
    b.remove_item(i1)
    assert b.get_total_cost()==decimal.Decimal('0')
    with pytest.raises(KeyError):
        b.items[i1]==0
def test_reset(i1,i2,b):
    """Given the basket is filled with item, 
    When the basket is reset, 
    That the basket becomes empty, 
    and That the total cost is 0
    """
    b.update_item(i1,10)
    assert b.is_empty()==False
    b.reset()
    assert b.is_empty()==True
    assert b.get_total_cost()==decimal.Decimal('1.52')*0
def test_error(i1,i2,b):
    with pytest.raises(ValueError,match="Quantity must be a positive number"):
        b.add_item(i1,-1)
