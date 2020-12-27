# lambda function
# lambda arguments: expression

sum = lambda x,y: x+y

print(sum(10,15))

# filter
numbers_list = [1,2,3,4,5,6]
even_list = list(filter(lambda x: x%2==0, numbers_list))
print(even_list)

# map
numbers_list = [1,2,3,4,5,6]
square_numbers_list = list(map(lambda x: x*x, numbers_list))
print(square_numbers_list)