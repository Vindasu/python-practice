# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    num_items = len(values)
    # Guard clause (early return)
    if num_items == 0:
        return None
    sum = 0
    for value in values:
        sum += value
    return sum / num_items
