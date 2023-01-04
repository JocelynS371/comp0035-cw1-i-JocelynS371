import pytest
import decimal

def test_add_item(i1, i2, b):
    """
        Given item entered is valid,
        When item is added to basket,
        Then ensure item is added to the list,
        and the new total is updated """
    b.add_item(i1, 1)
    assert b.is_empty() is False
    assert b.get_total_cost() == decimal.Decimal('1.52')


def test_remove_item(i1, b):
    """
        Given item entered is valid,
        When item is removed to basket,
        Then ensure item is removed from the list,
        and the new total is updated """
    b.update_item(i1, 10)
    b.remove_item(i1, 2)
    assert b.items[i1] == 10-2
    assert b.get_total_cost() == decimal.Decimal('1.52')*8
    b.remove_item(i1)
    assert b.get_total_cost() == decimal.Decimal('0')
    with pytest.raises(KeyError):
        b.items[i1] == 0


def test_reset(i1, b):
    """
        Given the basket is filled with item,
        When the basket is reset,
        That the basket becomes empty,
        and That the total cost is 0
    """
    b.update_item(i1, 10)
    assert b.is_empty() is False
    b.reset()
    assert b.is_empty() is True
    assert b.get_total_cost() == decimal.Decimal('1.52')*0


def test_error(i1, b):
    """
        Given item entered is valid,
        When an negative number is entered,
        That the basket returens an exception
    """
    with pytest.raises(ValueError, match="Quantity must be a positive number"):
        b.add_item(i1, -1)


@pytest.mark.parametrize('number',[-1, 0, 0.5, 62934, 9999999999, 3.14159,'test'])
def test_edge_case(i1, b, number):
    """ 
    This test the ability of the code to
    identify wrong values and handles them
    """
    if number % 1 != 0:
        with pytest.raises(expected_exception=[TypeError, ValueError]):
            b.add_item(i1, number)
    elif number is str:
        with pytest.raises(expected_exception=[TypeError, ValueError]):
            b.add_item(i1, number)
    elif number >= 1:
        b.add_item(i1, number)
        assert b.is_empty() is False
        assert b.get_total_cost() == i1.price*number
    elif number <= 0:
        with pytest.raises(expected_exception=ValueError, match="Quantity must be a positive number"):
            b.add_item(i1, number)
    else: raise ValueError("unknown input")
