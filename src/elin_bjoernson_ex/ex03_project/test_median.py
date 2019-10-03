# -*- coding: utf-8 -*-
import pytest

__author__ = "Elin Bjoernson"
__email__ = "elinbj@nmbu.no"


def median(data):
    """
    Function from exercise text.
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sorted_data = sorted(data)
    num_elements = len(sorted_data)
    if num_elements == 0:
        raise ValueError('Empty list')
    if num_elements % 2 == 1:  # if odd number
        return sorted_data[num_elements // 2]  # return number in middle
    else:  # if even number
        return (
            sorted_data[num_elements // 2 - 1] + sorted_data[num_elements // 2]
        ) / 2  # return average of two middle numbers


@pytest.fixture
def example_list():
    return [3, 5, 1, 2, 7, 0]


def test_median_of_singleton():
    assert median([4]) == 4


def test_median_raises_value_error_on_empty_list():
    """Test checking that requesting the median of an empty list raises a
    ValueError exception"""
    with pytest.raises(ValueError):
        median([])


def test_odd_numbers():
    """Tests that median function works for list with odd number of elements
    """
    odd_list = [4, 2, 9, 3, 5]
    assert median(odd_list) == 4


def test_even_numbers():
    """Tests that median function works for list with even numbers of elements
    """
    even_list = [1, 4, 5, 2]
    assert median(even_list) == 3


def test_ordered_numbers(example_list):
    """Tests that median function works for ordered elements
    """
    sorted_data = sorted(example_list)
    assert median(sorted_data) == 2.5


def test_reverse_ordered_numbers(example_list):
    """Tests that median function works for reverse-ordered elements"""
    sorted_data = sorted(example_list)
    sorted_data.reverse()
    assert median(sorted_data) == 2.5


def test_unordered_numbers(example_list):
    """Tests that median function works for unordered elements"""
    assert median(example_list) == 2.5


def test_original_unchanged(example_list):
    """Tests that median function leaves the original data unchanged"""
    median(example_list)
    assert example_list == [3, 5, 1, 2, 7, 0]


def test_tuples():
    """Tests that median function works for tuples"""
    tuple_data = (1, 8, 2, 3, 5)
    assert median(tuple_data) == 3
