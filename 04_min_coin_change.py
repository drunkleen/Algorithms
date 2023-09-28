import sys

map_dict = {}

def min_change(amount: int, coins: list[int]) -> list:
    if amount == 0:
        return 0
    
    if amount < 0:
        return -1
    
    if amount in map_dict:
        return map_dict.get(amount)
    
    min_coins = -1
    for coin in coins:
        sub_amount = amount - coin
        sub_coins = min_change(sub_amount, coins)
        if sub_coins != -1:
            num_coins = sub_coins + 1
            if num_coins < min_coins or min_coins == -1:
                min_coins = num_coins

    map_dict[amount] = min_coins
    return min_coins

amount = 502642
coins = [1, 2, 5, 10, 20, 50]

# to skip the "RecursionError"
sys.setrecursionlimit(amount*2) 

print(min_change(amount=amount,coins=coins))