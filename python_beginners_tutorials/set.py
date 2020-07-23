# Set is an unordered collection of objects

# Creating a set
empty_set = set()
non_empty_set = set([1,2,3,4,5])
print(non_empty_set)
set2 = {1,2,3,4,66,6}
print(set2)


# Properties of Set
# 1- Sets are unordered
numbers_set = {1, 12, 13, 23, 35, 46}
print(numbers_set[1])



# 2- Set elements are unique. Duplicate elements are not allowed.
numbers_set = {1, 2, 3, 4, 4, 5, 5, 5}
print(numbers_set)


# 3- A set itself may be modified, but the elements contained in the set
# must be of an immutable type.
type_set = {1, 1.5, 'str', (1,3,2)}
print(type_set)
mut_set = {[1,2,3]}

# Size and membership
members = {'x', 'y', 'z'}
print(len(members))
print('a' in members)


# Modifying set
numbers_set = {10,22,35,4,25,16,7}
numbers_set.add(55)
numbers_set.pop()
numbers_set.remove(221)
numbers_set.discard(221)
print(numbers_set)

# Mathematical Set operations
# Union
a_set = {1,2,3,4}
b_set = {3,4,5,6}
print(a_set | b_set)
print(a_set.union([3,4,5,6]))
print(a_set | [3,4,5,6])


# Intersection
a_set = {1,2,3,4}
b_set = {3,4,5,6}
print(a_set & b_set)
print(a_set.intersection(b_set))

# Difference
a_set = {1,2,3,4}
b_set = {3,4,5,6}

print(a_set - b_set)
print(a_set.difference(b_set))


# FrozenSet
frozen_set = frozenset([1,2,3,4,5])
frozen_set.remove(3)
print(frozen_set)