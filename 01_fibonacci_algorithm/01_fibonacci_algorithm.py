import sys

# https://en.wikipedia.org/wiki/Fibonacci_sequence
"""
In mathematics, the Fibonacci sequence is a sequence in which each
number is the sum of the two preceding ones. The Fibonacci numbers
may be defined by the recurrence relation.

F(n) = F(n-1) + F(n-2)
where F(0) = F(1) = 1
"""

map_dict = {} 
def fib(n:int):
    if n == 0 or n == 1: return n

    if n in map_dict: return map_dict[n]

    result = fib(n - 1) + fib(n - 2)
    map_dict[n] = result
    return result

num:int = 50

# to skip the "RecursionError"
sys.setrecursionlimit(num*2)


print(f"\n the {num}th fibonacci num is:\n", fib(num), "\n")
