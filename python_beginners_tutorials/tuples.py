# Creating Tuples
empty_tuple = ()
non_empty_tuple = (1,3,4)
print(non_empty_tuple)

# Concatenation of tuples
tuple1 = ("rashid", "ahmed", "raza")
tuple2 = (1, 3, 4)
print(tuple1 + tuple2)


# nested tuples
tupl3 = (3,4,5)
tupl4 = (4,7,8)
tuple5 = (tupl3, tupl4)
print(tuple5)


# repetition in tuples
name = ('rashid',) * 10
print(name)


# Accessing elements inside tuple
fruits = ("Mango", "Orange", "Grapes", "Melon", "Apple")
print(fruits[2])
print(fruits[1:4])

# tuples are immutable
numbers = (10, 15, 4, 13, 14)
# numbers[1] = 20


# length of tuple
numbers2 = (1, 2, 3, 5, 6)
print(len(numbers2))


# converting list into a tuple
tuple5 = (3, 5, 6, 1, 3)
list5 = list(tuple5)
list5[2] = 7
tuple5 = tuple(list5)
print(tuple5)


