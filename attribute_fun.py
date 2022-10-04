class MyObj:
	pass


my_obj = MyObj()
setattr(my_obj, 'caca', 'shit')
print(f'Added attr using "setattr(my_obj, \'caca\', \'shit\')" is {my_obj.caca}')

my_obj.dodo = 'cica'

print(f'Added attr using dot notation "my_obj.dodo = \'cica\'" is {my_obj.dodo}')

MyObj.class_attr = 'aha'
print(f'A class attribute "MyObj.class_attr = \'aha\'" added retroactively to all instances is {my_obj.class_attr}')

# What is the proper way in Python to check if a class has an attribute?
# Below throws "AttributeError: type object 'MyObj' has no attribute 'class_attr2'"
#if MyObj.class_attr2 is not None:
#	print(f'"MyObj.class_attr" has been set')


