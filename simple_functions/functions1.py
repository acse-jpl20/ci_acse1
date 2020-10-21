from functools import lru_cache

__all__ = ['my_sum', 'factorial', 'sin']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    return n * factorial(n-1) if n else 1

def sin(x_value, number):
    bruh = sum([((-1)**i*x_value**(2*i+1)/factorial(2*i+1)) for i in range(number)])
    return bruh
