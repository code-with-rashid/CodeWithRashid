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