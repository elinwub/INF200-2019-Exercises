# -*- coding: utf-8 -*-

__author__ = 'Elin Wølner Bjørnson'
__email__ = 'elinbj@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        """ Returns the next random number"""
        a = 7**5
        m = 2**31-1
        next_num = (a * self.seed) % m
        self.seed = next_num
        return next_num


class RandIter:
    def __init__(self, random_number_generator, length):
        """

        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        pass

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated. """
        pass
