class First(object):
	tasks = [1, 2, 3]


#class Second(First):
class Second(object):
	"""
	The commented line above gives
	/usr/local/bin/python3.9 /Users/jmquij0106/git/python-practice/multi_inheri.py
    Traceback (most recent call last):
      File "/Users/jmquij0106/git/python-practice/multi_inheri.py", line 9, in <module>
        class Third(First, Second):
    TypeError: Cannot create a consistent method resolution
    order (MRO) for bases First, Second
    [REF|https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance|""]
	"""
	tasks = [4, 5, 6]


class Third(First, Second):
	#tasks = [7, 8, 9]
	pass


print(f'tasks is {Third.tasks}')