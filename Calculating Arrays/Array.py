import numpy as np 

'''
@Author: Matheus Barros
Date: 03/01/2021

'''

array = np.array([
	
	[90, 92, 75, 60],
	[25, 20, 15, 90],
	[65, 130, 60, 75],

])

print('Array:\n',array)

#=========== MEAN OF EVERYTHING ===========
total_mean = array.mean()
print('\nThe number {} is the total mean of the array.\n'.format(total_mean))

#=========== CALCULATE THE MEAN OF COLUMNS, BASED ON ROWS NUMBERS ===========
array_mean_axis_0 = array.mean(axis = 0)
print('Mean with Axis = 0 \n{}'.format(array_mean_axis_0))

#=========== CALCULATE THE MEAN OF ROWS, BASED ON COLUMNS NUMBERS ===========
array_mean_axis_1 = array.mean(axis = 1)
print('\nMean with Axis = 1 \n{}'.format(array_mean_axis_1))