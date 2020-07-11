# List comprehension Signature:
# new_list = [expression for member in iterable (if conditional)]


# Problem 1:
# input: list of numbers
numbers = [1, 2, 2, 3, 4]
# required output: print square of numbers

# Method 1: map function
print(list(map(lambda n:n*n, numbers)))


# Method 2: for loop
square = []
for n in numbers:
    square.append(n * n)
print(square)


# Method 3: list comprehension
print([n*n for n in numbers])


# Method 4: set comprehension
print({n*n for n in numbers})


# Method 4: dictionary comprehension
print({f'square_{n}':n*n for n in numbers})


# Problem 2:
# input: string
sentence = 'the rocket came back from mars'
# required output: print all the vowels in the sentence


# Method 1: filter function
print(list(filter(lambda chr: chr in 'aeiou', sentence)))

# Method 2: for loop
vowels = []
for v in sentence:
    if v in 'aeiou':
        vowels.append(v)
print(vowels)

# Method 3: list comprehension
print([v for v in sentence if v in 'aeiou'])

# Method 4: set comprehension
print({v for v in sentence if v in 'aeiou'})
