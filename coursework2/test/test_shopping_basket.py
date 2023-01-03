import pytest
from coursework2.src.shopping_basket import Basket
from coursework2.src.shopping_basket import Item

import decimal
from decimal import Decimal
from reprlib import recursive_repr

def test_add_item():
    """ Given item entered is valid, 
    When item is added to basket, 
    Then ensure item is added to the list, 
    and the new total is updated """
    i1 = Item("Warburtons", "Toastie", "800g white sliced loaf", decimal.Decimal('1.52'))
    b=Basket()
    b.add_item(i1, 1)
    assert b.is_empty==False
    assert b.get_total_cost==1.52
    print(i1)
test_add_item()


