# -*- coding: utf-8 -*-
import pytest
#from .median import median
__author__ = "Elin Bjoernson"
__email__ = "elinbj@nmbu.no"

# function from exercise text
def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sorted_data = sorted(data)
    num_elements = len(sorted_data)
    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    else:
        return (
            sorted_data[num_elements // 2 - 1] + sorted_data[num_elements // 2]
        ) / 2


def test_median_of_singleton():
    assert median([4]) == 4


def test_median_raises_value_error_on_empty_list():
    """Test checking that requesting the median of an empty list raises a
    ValueError exception"""
    with pytest.raises(ValueError):
        median([])
    # supposed to fail?
    #samme som:
    #try:
    #    median([])
    #except ValueError:
    #    pass
    #else:
    #    assert False


def test_odd_numbers():
    """Tests that median works on list with odd number of elements
    Returns
    -------

    """


def test_even_numbers():
    """Tests that median works on list with even numbers of elements
    """


def test_ordered_numbers():
    """Tests that median works on ordered elements
    """


def test_reverse_ordered_numbers():
    """Tests that median works on reverse-ordered elements"""


def test_unordered_numbers():
    """Tests that median works on unordered elements"""


def test_original_unchanged():
    """Tests that median function leaves the original data unchanged"""


def test_tuples():
    """Tests that median function works for tuples"""
