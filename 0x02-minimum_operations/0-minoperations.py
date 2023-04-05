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
        int: The number of minimal operations needed to get n characters
    or 0 if it is impossible to achieve n.
    """
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            done += clipboard
            ops_count += 1
    return ops_count