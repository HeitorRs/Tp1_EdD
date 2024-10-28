def greatestNumber(array):
    max_number = array[0]

    for num in array:
        if num > max_number:
            max_number = num

    return max_number

array = [2, 4, 6, 8, 10, 12, 13]
print(greatestNumber(array))