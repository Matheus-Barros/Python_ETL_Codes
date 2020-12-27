import pandas as pd
import json

'''
@Author: Matheus Barros 
Date: 27/12/2020

'''

#========== Load the daily report to a data frame ==========
try:
	df = pd.read_json('unece.json')
	print(df)
	df.to_excel('aki.xlsx', index = False)

except Exception as e:
	print(e)