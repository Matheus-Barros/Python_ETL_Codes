import pandas as pd 

'''
@Author: Matheus Barros
Date: 03/01/2021

'''

try:

	car_cols = {'Car_Name':['Civic','A3','M6','Corolla','AMG GT'],
				'id_Manufactory_FK':[21,33,55,76,11]}

	df_CarNames = pd.DataFrame(data = car_cols)

	new_cars = []
	#=========== ITERATING WITH ITERROWS METHOD ===========
	for i,row in df_CarNames.iterrows():
		car = row['Car_Name']
		new_cars.append('CRV')
		print(car)

	#=========== WRITING IN THE DATAFRAME ===========	
	df_CarNames['Car_Name'] = new_cars
	print(df_CarNames)		
	
except Exception as e:
	print(e)