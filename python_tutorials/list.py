# List is an ordered collection of arbitrary objects.
# Signature:
# [element1, element2, ,..., elementN]











# Properties of Lists:
# ---------------------------------------------
# 1 => Lists are ordered.
list1 = [1,2,3,4]
list2 = [1,3,2,4]
# print(list1==list2)



# ---------------------------------------------
# 2 => Lists can contain any arbitrary objects.
list1 = [1,1.5, 'string']
# print(list1)

# Lists can even contain complex objects, like functions, classes, and modules
sum = lambda x,y: x+y
list2 = [int, float, str, sum]
# print(list2)




# ---------------------------------------------
# 3 => List elements can be accessed by index.
numbers = [2,5,3,7,6,10,11]
# print(numbers[-5:-1])
# print(numbers[2:5])
# print(numbers[:5])
# print(numbers[1:])
# print(numbers[:])
# print(numbers[1])
# print(numbers[0])
# print(numbers[4])
# print(numbers[-1])
# print(numbers[-2])







# ---------------------------------------------
# 4 => Lists can be nested to arbitrary depth.
# numbers = [1,2,3, [4,5, [7,8,9]]]
# print(numbers[1])
# print(numbers[3][2][1])






# ---------------------------------------------
# 5 => Lists are mutable.
numbers = [9,20,10,27,5]
# print(numbers)
# numbers.sort()
# numbers.reverse()
# numbers.extend([10,11,12])
# del numbers[-1]
# numbers.remove(4)
# numbers.pop(2)
# numbers.insert(2, 11)
# numbers.append(10)
# numbers[2] = 7
# numbers[1:3] = [7,8]
# print(numbers)




# ---------------------------------------------
# 6 => Lists are dynamic.
# numbers = [1,2,3,4,5]
# print(numbers)
# numbers[1:3] = [10,20,30,40]
# print(numbers)
# del numbers[2]
# print(numbers)
# del numbers[3]
# print(numbers)



numbers = [10,20,35,4,5]
print(min(numbers))
print(max(numbers))
print(len(numbers))
print(sorted(numbers))