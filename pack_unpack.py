STAT_HEADERS = {'x-stat-contentVersion': 'STAT'}


def my_pack_func(first_arg, **kwargs):
	# kwargs has all the name/value pairs that caller passed, if any packed into single variable
	print(f'first arg is {first_arg}')
	for k, v in kwargs.items():
		print(f'k is {k} and v is {v}')


# I need to unpack STAT_HEADERS because my_pack_func() expects a variable number of keyword'ed arguments. If I
# didn't unpack then Python throws error that only on positional argument is expected. I guess this is somewhat
# analogous to JavaScript ...rest syntax
# my_pack_func('shit', STAT_HEADERS) # wrong, Python expects only one positional item
my_pack_func('shit', name="hi I'm name param", **STAT_HEADERS)
