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


@pytest.mark.parametrize('test_item,number',[('i1', 638), ('i1', 0),('i1', -1), ('i2', 23), ('i1', 9999999), ('i1', 0.5)])
def test_edge_case(i1, i2, b, test_item, number):
    if number % 1 != 0:
        with pytest.raises(expected_exception=[TypeError, ValueError]):
            b.add_item(test_item, number)
    elif number >= 1:
        b.add_item(test_item, number)
        assert b.is_empty() is False
        assert b.get_total_cost() == getattr(test_item,'price')*number
    else:
        with pytest.raises(expected_exception=ValueError, match="Quantity must be a positive number"):
            b.add_item(test_item, number)