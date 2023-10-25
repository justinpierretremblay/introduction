def compute_fibonacci(n):
    """Return the nth Fibonacci number.

    >>> compute_fibonacci(0)
    0
    >>> compute_fibonacci(1)
    1
    >>> compute_fibonacci(2)  # 0 + 1
    1
    >>> compute_fibonacci(3)  # 1 + 1
    2
    >>> compute_fibonacci(4)  # 1 + 2
    3
    """
    
    # BEGIN QUESTION 1.1
    i = 0
    result = [0] * (n+1)
    for i in range(n+1):
        if(i <= 0):
            result[i] = 0
        elif(i==1):
            result[i] = 1
        else:
            result[i] = result[i-1] + result[i-2]
    print(result[n])
    return result[n]


    # END QUESTION 1.1