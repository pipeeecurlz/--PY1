list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

list_max = 0
list_max_index = 0

for i, num in enumerate(list_numbers):
    if num >= list_max:
        list_max = num
        list_max_index = i

list_numbers[list_max_index], list_numbers[-1] = list_numbers[-1], list_numbers[list_max_index]

print(list_numbers)
