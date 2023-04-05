#!/usr/bin/python3
"""Task 0 task
"""


def minOperations(n):
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
    idef minOperations(n):
    """
    Single character H
    Fewest number of operations
    """

    if n <= 1:
        return 0
    numbr, index, operations = n, 2, 0

    while numbr > 1:
        if numbr % index == 0:
            numbr = numbr / index
            operations = operations + index
        else:
            index += 1
    return operations