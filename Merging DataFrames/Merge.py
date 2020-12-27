import pandas as pd
import requests
import json

'''
@Author: Matheus Barros 
Date: 28/12/2020

'''
try:
	car_cols = {'Car_Name':['Civic','A3','M6','Corolla','AMG GT'],
				'id_Manufactory_FK':[21,33,55,76,11]}

	manufactory_cols = {'id_Manufactory_PK':[11,21,76,33,55],
						'Manufactory':['Mercedes-Benz','Honda','Toyota','Audi','BMW']}
	df_CarNames = pd.DataFrame(data = car_cols)
	df_Manufactory = pd.DataFrame(data = manufactory_cols)
	

	merged_data = df_CarNames.merge(df_Manufactory,
									left_on = 'id_Manufactory_FK',
									right_on = 'id_Manufactory_PK')

	print('Original DataFrame:\n',merged_data,'\n\n--------------------------\n')
	print('Simplified DataFrame:\n',merged_data[['Car_Name','Manufactory']])







except Exception as e:
	print(e)