def binary_array_to_number(arr):
    i = 0
    number = 0
    sqrt2 = 1
    len_arr = len(arr)
    len_arr -= 1
    if arr[len_arr] == 1:
        number += 1
    len_arr -= 1
    while len_arr >= i:
        if arr[len_arr] == 1:
            sqrt2 *= 2
            number += sqrt2
            len_arr -= 1
        else:
            sqrt2 *= 2
            len_arr -= 1
    print(number)

binary_array_to_number([1, 1, 0, 0])