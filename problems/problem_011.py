# Complete the is_divisible_by_5 function to return the
# word "buzz" if the value in the number parameter is
# divisible by 5. Otherwise, just return the number.

def is_divisible_by_5(number):
    if int(number) % 5 == 0:
        return "buzz"
    else:
        return number
