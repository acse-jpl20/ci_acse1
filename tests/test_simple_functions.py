import pytest
from simple_functions import my_sum, factorial, sin
import numpy as np

class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected
    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer
    @pytest.mark.parametrize('value_of_x, long, expected', [
        (np.pi, 20, 0),
        (0, 20, 0),
        (np.pi/2, 20, 1)
    ])
    def test_sin(self, value_of_x, long, expected):
        '''Test our sin function'''
        answer = sin(value_of_x, long)
        assert np.isclose(answer, expected, atol=10e-3)
