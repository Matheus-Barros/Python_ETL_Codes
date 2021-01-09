import time
from functools import wraps

'''
@Author: Matheus Barros
Date: 09/01/2021

'''

#============ DEFINING DECORATORS ============
def counter(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		wrapper.count += 1
		# Call the function being decorated and return the result
		return func(*args, **kwargs)
	wrapper.count = 0
	# Return the new decorated function
	return wrapper

def timer(func):
	"""A decorator that prints how long a function took to run.
	"""
	# Define the wrapper function to return.
	@wraps(func)
	def wrapper(*args, **kwargs):
		# When wrapper() is called, get the current time.
		t_start = time.time()
		# Call the decorated function and store the result.
		result = func(*args, **kwargs)
		# Get the total time it took to run, and print it.
		t_total = time.time() - t_start
		print('{} took {}s'.format(func.__name__, t_total))
		return result

	return wrapper

#============ DEFINING FUNCTIONS ============
@counter
def print_my_name():
	"""
	A function that prints my name
	----------
	Returns
	-------
	str
		Prints my name
	"""
	print('Matheus')

@timer
def print_my_lastname():
	"""
	A function that prints my last name
	----------
	Returns
	-------
	str
		Prints my last name
	"""
	print('Barros')
	time.sleep(2)

#============ CALLING FUNCTIONS ============
print('Calling {} function'.format(print_my_name.__name__))
print_my_name()
print_my_name()

print('print_my_name() was called {} times.'.format(print_my_name.count))

print('\nCalling {} function'.format(print_my_lastname.__name__))
print_my_lastname()


accessing_not_decorated_print_my_lastname = print_my_lastname.__wrapped__
print('\nCalling {} function not decorated'.format(accessing_not_decorated_print_my_lastname.__name__))

print(accessing_not_decorated_print_my_lastname())
