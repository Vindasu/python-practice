# Complete the fizzbuzz function to return
# * The word "fizzbuzz" if number is evenly divisible by
#   by both 3 and 5
# * The word "fizz" if number is evenly divisible by only
#   3
# * The word "buzz" if number is evenly divisible by only
#   5
# * The number if it is not evenly divisible by 3 nor 5
#
# Try to combine what you have done in the last two problems
# from memory.

def fizzbuzz(number):
    if int(number) % 5 == 0 and int(number) % 3 == 0: 
        return "fizzbuzz"
    elif int(number) % 5 == 0:
        return "buzz"
    elif int(number) % 3 == 0:
        return "fizz"
    else:
        return number