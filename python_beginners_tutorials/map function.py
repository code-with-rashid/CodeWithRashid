# Signature:
# map(function, iterable [, iterable2, iterable3,....., iterableN])-->map object
# possible iterables: list, tuple, set

numbers = [1,2,3,4]
print(list(map(lambda x: x*x, numbers)))


first_name_list = ["Rashid", "Ahmed", "Ali"]
last_name_list = ["Mahmood", "Raza", "Hassan"]

print(list(map(lambda x,y: x+y, first_name_list,last_name_list)))