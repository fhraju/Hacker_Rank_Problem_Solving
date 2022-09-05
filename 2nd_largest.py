array = [2, 3, 7, 10, 90, 80, 30, 100, 200, 150]

first_largest_num = array[0]
for num in array:
    if num > first_largest_num:
        first_largest_num = num

second_largest_num = array[0]
for num in array:
    if num > second_largest_num and num < first_largest_num:
        second_largest_num = num

print(first_largest_num, second_largest_num)