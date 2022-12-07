from random import sample
def get_unique_list_numbers() -> list[int]:
    nums = [i for i in range(-10, 11)]
    unique_list = sample(nums, 15)

    return unique_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
