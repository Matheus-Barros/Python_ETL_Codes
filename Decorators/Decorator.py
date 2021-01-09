'''
@Author: Matheus Barros
Date: 08/01/2021

'''
#====== CREATING THE DECORATOR THE WILL DOUBLE THE ARGUMENTS OF THE FUNCTION ======
def double_args(func):
	def wrapper(a,b):
		return func(a * 2, b * 2)
	return wrapper


#====== CALLING THE DECORATOR ======
@double_args
def multiply(a, b):
	return a * b

print('Multiplication of values doubled:',multiply(1, 5))