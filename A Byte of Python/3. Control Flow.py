def binary_array_to_number(arr):
    s = 0
    for digit in arr:
        s = s * 2 + digit
        print(s)
        print(digit)

binary_array_to_number([1,0,0,1])