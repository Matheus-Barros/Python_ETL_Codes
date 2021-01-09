import time
from functools import wraps

'''
@Author: Matheus Barros
Date: 09/01/2021

'''

def run_n_times(n):
	"""Define and return a decorator"""
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			for i in range(n):
				func(*args, **kwargs)
		return wrapper
	return decorator

#============ DEFINING RUNNING TIMES ============
@run_n_times(5)
def print_hello():
	"""
	A function that prints Hello!
	----------
	Returns
	-------
	str
		Prints Hello!
	"""	
	print('Hello!')


print_hello()