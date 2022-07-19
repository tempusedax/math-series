def fibonacci(num):
    """
    # This code is contributed by Saket Modi
    :param num:
    :return:
    """
    if num < 0:
        print("Incorrect input")
    elif num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def lucas(num):
    if num == 0:
        return 2
    elif num == 1:
        return 1
    else:
        return lucas(num - 1) + lucas(num - 2)


def sum_series(num, p=0, q=1):
    if p == 1:
        return 2
    if q == 2:
        return 2

    return fibonacci(num - 1) + fibonacci(num - 2) + lucas(num - 1) + lucas(num - 2)


