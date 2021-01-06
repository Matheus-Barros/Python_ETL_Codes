import inspect

'''
@Author: Matheus Barros
Date: 05/01/2021

'''

#Google Style
def sum_two_values_method1(val1 , val2):
	"""Sum of values (MUST WRITTE IN IMPERATIVE)
	Args:
		val1 (int): Value to sum.
		val2 (int): Second value to sum.

	Returns:
		result: Result of the sum of both values.

	Raises:
		ValueError: Returns the variable 'e', if any of the parameters passed are invalid.

	Notes:
		See www.mathbarro.com for more info.
	"""
	try:
		result = val1 + val2
		return result
	
	except Exception as e:
		return e



#Numpydoc
def sum_two_values_method2(val1 , val2):
	"""
	Description of what the function does.
	Parameters
	----------
	val1 : int
		Value to sum.

	val2 : int
		Second value to sum.

	Returns
	-------
	int
		Result of the sum of both values.
	"""
	try:
		result = val1 + val2
		return result
	
	except Exception as e:
		return e


#Calling Functions
Test1 = sum_two_values_method1(1,3)
print(Test1,'\n++++++++\n')

Test2 = sum_two_values_method2('Invalid Value',3)
print(Test2,'\n++++++++\n')

#Retrieving docstrings
print(inspect.getdoc(sum_two_values_method1),'\n++++++++\n')
print(inspect.getdoc(sum_two_values_method2))






