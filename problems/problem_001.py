# Complete the minimum_value function so that returns the
# minimum of two values.
#
# If the values are the same, return either.

def minimum_value(value1, value2):
    if value1 < value2:
        return value1
    if value2 <= value1:
        return value2
