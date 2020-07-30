# A dictionary is collection of key-value pairs in Python.
# 1st method
person = {
    'name': 'Rashid',
    'gender': 'Male'
}
print(person)

# 2nd method
person = dict()
person['name']= 'Rashid'
person['gender']= 'Male'
print(person)

print(person['gender'])
print(len(person))
print(person.keys())
print(person.values())
del person['gender']
print(person)


car_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Changing value of a specific item
car_dict['year'] = 2000
print(car_dict)

# Check if key exists in the dictionary
print('model' in car_dict)

# Adding item to a dictionary
car_dict['color'] = 'Black'
print(car_dict)

# Adding dictionary to a dictionary
car_dict2 = {
    'width': '75.4 in',
    'height': '54.3 in'
}
car_dict.update(car_dict2)
print(car_dict)

# Removing a particular item from the dictionary
print(car_dict.pop('year2', 'Not Found'))
print(car_dict)

# Remove last inserted item
car_dict.popitem()
print(car_dict)