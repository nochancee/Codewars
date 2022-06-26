def digital_root(n):
    result = 0
    n_list = [int(i) for i in str(n)]
    print(n_list)
    for i in n_list:
        result += i
    while result >= 10:
        if result == 10:
            result = 1
            return(result)
        elif result >= 10:
            n_list = [int(i) for i in str(result)]
            result = 0
            for i in n_list:
                result += i
    return(result)