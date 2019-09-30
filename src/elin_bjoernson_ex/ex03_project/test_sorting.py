# -*- coding: utf-8 -*-

__author__ = 'Elin Bjoernson'
__email__ = 'elinbj@nmbu.no'


def bubble_sort(numbers):
    new_list = list(numbers)
    for _ in new_list:
        for idx, num in enumerate(new_list):
            if idx == len(new_list) - 1:  # if last element, do nothing
                pass
            elif num > new_list[idx + 1]:
                new_list.insert(idx + 1, new_list.pop(idx))
    return new_list


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data != data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    bubble_sort(data)
    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [1, 2, 3]
    sorted_data = bubble_sort(data)
    sort_sorted = bubble_sort(sorted_data)
    assert sort_sorted == sorted_data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [1, 3, 2]
    reverse_sorted = bubble_sort(data)[::-1]
    assert bubble_sort(reverse_sorted) == sorted(data)


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [1, 2, 1]
    assert bubble_sort(data) == sorted(data)


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    data = ([1],
            [1, 20, 3, 5],
            [9, 8, 7],
            [12, 20, 11, 109],
            [9, 2, 88, 3, 10, 22])
    for numbers in data:
        sorted_data = bubble_sort(numbers)
        assert sorted_data == sorted(numbers)
