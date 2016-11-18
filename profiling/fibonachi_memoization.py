# -*- coding: utf-8 -*-


def memoization(function):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper





@memoization
def fib(n):
    return 1 if n <= 1 else fib(n-1) + fib(n-2)

print(fib(0), fib(1), fib(2), fib(3), fib(4), fib(5), fib(6))
print(fib(100))

decorated_fibonachi = memoization(fib)

print(decorated_fibonachi(100))