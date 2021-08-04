"""
[REF|https://realpython.com/python-keyerror/|""]
"""

my_dict = {'shit': 'crap'}

# Below raises KeyError exception because gthe key is not in the dictionary. I guess Python designers
# preferred an error be raised early on to avoid the dreaded NPE type exception raised in Java which happens when you
# would go to dereference a property of a 'null' object
# print(my_dict['foo'])

# Below does not work like Groovy's default Map.get('key', 'default val'), because it will not
# insert the default, just returns it...
print(my_dict.get('foo', 'bar'))

# ...below does
print(my_dict.setdefault('bull', 'dong'))

print(my_dict)
