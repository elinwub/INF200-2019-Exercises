# -*- coding: utf-8 -*-

__author__ = 'Elin Bjoernson'
__email__ = 'elinbj@nmbu.no'

# function from exercise text
def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
        else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))
