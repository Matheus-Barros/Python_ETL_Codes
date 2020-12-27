import pandas as pd 

'''
@Author: Matheus Barros 
Date: 26/12/2020

'''
#========== SETING THE DATA TYPES ==========
dtype_dic = {'Name':str,'Took_English_Course':bool}

#========== SPECIFING TRUE AND FALSE VALUES ==========
df = pd.read_excel('BoolValues.xlsx',
					dtype = dtype_dic,
					true_values=['Yes','Yeah',1],
					false_values=['No',0,''],
					keep_default_na=False)

print(df)