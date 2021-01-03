import pandas as pd 

'''
@Author: Matheus Barros
Date: 03/01/2021

'''

try:

	def to_BRL(Price_USD):
		price_BRL = int(Price_USD * 6.45)
		return price_BRL

	

	price_BRL_lst = []

	car_cols = {'Car_Name':['Civic','A3','M6','Corolla','AMG GT'],
				'Price_USD':[21000,33000,55000,7600,11000]}

	df_CarNames = pd.DataFrame(data = car_cols)

	#=========== ITERATING WITHOUT LOOP WITH LAMBDA ===========
	price_BRL_lst = df_CarNames.apply(
										lambda row: to_BRL(row['Price_USD']),
										axis = 1
									)
	df_CarNames['Price_BRL'] = price_BRL_lst

	print(df_CarNames)


except Exception as e:
	print(e)