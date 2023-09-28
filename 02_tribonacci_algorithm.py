import sys

"""
The Tribonacci series algorithm prints a sequence where each term is
the sum of the three preceding terms. It starts with the initial values of
0, 0, and 1. It can be defined as

t(n) = t(n-1) + t(n-2) + t(n-3)
where t(0) = t(1) = 0, t(2) = 1
"""
map_dict = {} 
def tri(n:int):
    if n == 0 or n == 1: return 0
    elif n == 2: return 1

    if n in map_dict: return map_dict[n]

    result = tri(n - 1) + tri(n - 2) + tri(n - 3)
    map_dict[n] = result
    return result

num:int = 6

# to skip the "RecursionError"
sys.setrecursionlimit(num*2)


print(f"\n the {num}th tribonacci num is:\n", tri(num), "\n")
