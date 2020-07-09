# Signature:
# map(function, iterable [, iterable2, iterable3,...iterableN])-->map object
# possible iterables: list, tuple, set

# ---------------------------------------------
# list of string number
num_list = ['4', '10', '20', '100', '138']
# convert string numbers into integers
print(list(map(int, num_list)))

# ---------------------------------------------
first_name_ls = ['Kashif', 'Ahsan', 'Waqas']
last_name_ls = ['Raza', 'Ali', 'Yousaf']
# return list of full names.
full_name = lambda x,y: "%s %s" % (x,y)
print(list(map(full_name, first_name_ls, last_name_ls)))