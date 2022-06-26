def tribonacci(signature, n):
    i = 2
    if n == 0:
        signature.clear()
    elif n == 1:
        del signature[1]
        del signature[1]
    elif n == 2:
        del signature[2]
    else: 
        while i <= (n-2):
            number1 = signature[i]
            number2 = signature[i-1]
            number3 = signature[i-2]
            next_tribonacci_nubmer = number1+number2+number3
            signature.append(next_tribonacci_nubmer)
            i +=11
    print(signature)