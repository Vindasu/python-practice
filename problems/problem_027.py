# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#
def max_in_list(values):
    if values == []:
        return None
    num = values[0]
    for value in values:
        if value >= num:
            num = value

    return num
