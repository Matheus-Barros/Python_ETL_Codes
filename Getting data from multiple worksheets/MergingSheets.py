import pandas as pd 

'''
@Author: Matheus Barros 
Date: 26/12/2020

'''
#========== Getting all sheets at once ==========
MultipleSheets = pd.read_excel('MultipleSheets.xlsx',sheet_name = None)

#========== Create empty data frame to hold all loaded sheets ==========
all_responses = pd.DataFrame()

#========== Iterate through data frames in dictionary ==========
for sheet_name, df in MultipleSheets.items():

	#========== Add a column so we know which year data is from ==========
	df["SHEET_NAME"] = sheet_name

	#========== Add each data frame to all_responses ==========
	all_responses = all_responses.append(df)

	#========== Reseting indexes ==========
	all_responses = all_responses.reset_index(drop=True)

#========== View sheet's names merged ==========
print(all_responses.SHEET_NAME.unique())
