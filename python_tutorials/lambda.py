def sum(a,b):
    return a+b

print(sum(10,12))

sum2 = lambda a,b: a+b
print(sum2(5,10))

num_list = ['id12', 'id2', 'id100', 'id50']
print(sorted(num_list))

print(sorted(num_list, key=lambda x:int(x[2:])))

name_list = ["Rashid", "  ahmed", "raza    "]
print(list(map(lambda x:x.strip().upper(), name_list)))

num_list2 = [1,2,3,4,5,6,7,8]
print(list(filter(lambda x:x%2==0, num_list2)))