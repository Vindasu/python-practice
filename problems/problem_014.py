# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.


def can_make_pasta(ingredients):
    return (
        "flour" in ingredients
        and "eggs" in ingredients
        and "oil" in ingredients)

    # found_flour = False
    # found_eggs = False
    # found_oil = False
    # for ingredient in ingredients:
    #     if ingredient == "flour":
    #         found_flour = True
    #     if ingredient == "eggs":
    #         found_eggs = True
    #     if ingredient == "oil":
    #         found_oil = True
    # return found_flour and found_eggs and found_oil
