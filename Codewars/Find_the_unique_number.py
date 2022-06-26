def find_uniq(arr):
    import copy
    arr_copy = copy.deepcopy(arr)
    arr_copy.pop(0)
    for j in arr:
        for n in arr_copy:
            if arr[0] != arr_copy[0] and arr[1] == arr_copy[1]:
                n = arr[0]
                print(n)
                return(n)
            elif j != n:
                print(n)
                return (n)