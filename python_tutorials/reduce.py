# Signature:
# functools.reduce(function, iterable[, initializer])
# possible iterables:  lists, tuples, range objects, generators,
# iterators, sets, dictionary keys and values












# ---------------------------------------------
# input: list of numbers.
numbers = [0, 1, 2, 3, 4]
# required output: print sum of numbers.
def my_add(a, b):
	result = a + b
	print(f"{a} + {b} = {result}")
	return result
from functools import reduce
# print(reduce(my_add, numbers, 100))











# ---------------------------------------------
# input: list of numbers.
numbers = [15, 5, 10, 26, 3, 1]
# required output: print minimum and maximum numbers.
max_func = lambda x,y: x if x>y else y
min_func = lambda x,y: x if x<y else y
# print("Max: %d" % reduce(max_func, numbers))
numbers = []
print("Min: %d" % reduce(min_func, numbers, 0))