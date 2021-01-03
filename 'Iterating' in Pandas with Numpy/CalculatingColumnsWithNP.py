import pandas as pd
import numpy as np 

'''
@Author: Matheus Barros
Date: 03/01/2021

'''
try:

	cols = {'Value1':[21000,33000,55000,7600,11000],
				'Value2':[1000,3000,5000,600,1000]}

	df_values = pd.DataFrame(data = cols)


	#=========== CREATING A NEW ARRAY WITH THE VALUES DIFFERENCES (RETURNS AN ARRAY)===========
	values_diffs = df_values['Value1'].values - df_values['Value2'].values

	#=========== CREATING NEW COLUMN WITH THE VALUES DIFFERENCES ===========
	df_values['Values_diffs'] = values_diffs

	print(df_values)

except Exception as e:
	print(e)