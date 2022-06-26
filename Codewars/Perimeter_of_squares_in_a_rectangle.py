def perimeter(n):
    n = n+1
    fib1 = fib2 = 1
    fib_sum = 2
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        fib_sum += fib2
    return(fib_sum*4)