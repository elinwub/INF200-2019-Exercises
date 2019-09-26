# -*- coding: utf-8 -*-

__author__ = 'Elin Bjoernson'
__email__ = 'elinbj@nmbu.no'


def bubble_sort(numbers):
    new_list = list(numbers)
    for _ in new_list:
        for idx, num in enumerate(new_list):
            if idx == len(new_list)-1:  # if last element, do nothing
                pass
            elif num > new_list[idx+1]:  # if higher value than next element, exchange them
                new_list.insert(idx+1, new_list.pop(idx))
    return new_list


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1),):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))


    def test_empty():
        """Test that the sorting function works for empty list"""
pass


def test_single():
    """Test that the sorting function works for single-element list"""
    pass


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    pass


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    pass


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    pass


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    pass


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    pass


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    pass