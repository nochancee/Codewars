def count_bits(n):
    count_1 = 0
    for i in bin(n):
        if i == '1':
            count_1 += 1
    return(count_1)

def countBits(n):
    return bin(n).count("1")