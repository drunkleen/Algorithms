map_dict = {} 
def sum_possible(amount: int, numbers: list[int]) -> bool:
    if amount == 0:
        return True
    if amount < 0:
        return False
    
    if amount in map_dict:
        return map_dict.get(amount)

    for num in numbers:
        sub_amount = amount - num
        if sum_possible(sub_amount, numbers):
            map_dict[amount] = True
            return True
    
    map_dict[amount] = False
    return False

amount = 8
numbers= [2, 4, 6, 8]

print(sum_possible(amount=amount, numbers=numbers))
