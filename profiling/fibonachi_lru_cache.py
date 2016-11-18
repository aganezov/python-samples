# -*- coding: utf-8 -*-
from functools import lru_cache


@lru_cache(maxsize=256)
def fib(n):
    return 1 if n <= 1 else fib(n-1) + fib(n-2)


print(fib(0), fib(1), fib(2), fib(3), fib(4), fib(5), fib(6))
print(fib(100))
