from random import randint

def get_unique_list_numbers(min=-10, max=10, size=15) -> list[int]:
    list_ = []
    i = 0
    while i < size:
        x = randint(min, max)
        if x not in list_:
            list_.append(x)
            i += 1
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
