'''
@Author: Matheus Barros
Date: 08/01/2021

'''
x = 20
y = 60
print('Original variable x:',x)
print('Original variable y:',y)

def function1():

	global x
	x = 50
	y = 10
	print('Declare a copy of variable y locally:',y)

	def function2():
		nonlocal y
		y = 15
	
	print('Change the variable y only inside the function:',y)

	function2()

function1()

print('Result of variable x:',x)
print('Result of variable y:',y)

