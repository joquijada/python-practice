import random

"""
[REF|https://realpython.com/python-keyerror/|""]
"""

my_dict = {'shit': 'crap'}

# Below raises KeyError exception because the key is not in the dictionary. I guess Python designers
# preferred an error be raised early on to avoid the dreaded NPE type exception raised in Java which happens when you
# would go to dereference a property of a 'null' object
# print(my_dict['foo'])

# Below is one way to check if a dictionary contains a key,
# https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
print('foo' in my_dict)
print('shit' in my_dict)

# Below does not work like Groovy's default Map.get('key', 'default val'), because it will not
# insert the default, just returns it...
print(my_dict.get('foo', 'bar'))

# ...below does
print(my_dict.setdefault('bull', 'dong'))

print(my_dict)

# Accessing dictionaries, can't use index, below throws KeyError
# print(my_dict[0])

# Below outputs the keys of dictionary as an object of type 'dict_keys', which is an iterable
# and therefore can be used inside a 'for' loop
my_keys = my_dict.keys()
print(my_keys)
for key in my_keys:
    print(key)

# ...and so does this
print(list(my_dict))

# Randomly select a key/val pair from a dictionary, [REF|https://stackoverflow.com/questions/4859292/how-to-get-a-random-value-from-dictionary|"and now asks for a pair"]
print(random.choice(list(my_dict.items())))

# self.http_headers.update({'x-stat-contentVersion': 'OTT'})
print(my_dict['shit'])

my_dict.update({'addedWithUpdateKey': 'addedWithUpdateValue'})
print(my_dict)
