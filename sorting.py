#  1. You will be sorting the following list by each element’s second letter a to z.
# Create a function to use when sorting that takes a string as input and return the second letter
# of that string and name it second_let. Create a variable called func_sort and assign
# the sorted list to it. Do not use lambda.

# ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
#
# def second_let(s):
#     return s[1]
# func_sort = sorted(ex_lst,key = second_let)

# ________________________________________

# 2. Below, we have provided a list of strings called nums. Write a function called last_char
# that takes a string as input, and returns only its last character.
# Use this function to sort the list nums by the last digit of each number,
# from highest to lowest, and save this as a new list called nums_sorted.

# nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
#
# def last_char(s):
#     return s[-1]
#
# nums_sorted = sorted(nums,key = last_char, reverse = True)

# ________________________________________


# 3. Once again, sort the list nums based on the last digit of each number from
# highest to lowest. However, now you should do so by writing a lambda function.
# Save the new list as nums_sorted_lambda.

# nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
# a = lambda x: x[-1]
# nums_sorted_lambda = sorted(nums,key = a,reverse = True)

# ________________________________________