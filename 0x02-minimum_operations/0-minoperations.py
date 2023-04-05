#!/usr/bin/python3
"""Task 0 task
"""



    """The function alculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               number of min operations
    Args:
        n (int): The number of desired n characters.
    Returns:
        int: The number of minimal operations needed to get ncharacters
    or 0 if it is impossible to achieve n.
    """


    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter