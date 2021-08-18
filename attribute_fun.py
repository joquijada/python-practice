class MyObj:
	pass


my_obj = MyObj()
setattr(my_obj, 'caca', 'shit')
print(f'Added attr is {my_obj.caca}')