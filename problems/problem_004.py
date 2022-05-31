# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

def max_of_three(value1, value2, value3):
    num = value1
    if value2 >= num:
        num = value2
    if value3 >= num:
        num = value3
    return num


#     if value1 >= value2 >= value3:
#         return value1
#     elif value2 >= value1 >= value3:
#         return value2
#     elif value3 >= value1 >= value2:
#         return value3


