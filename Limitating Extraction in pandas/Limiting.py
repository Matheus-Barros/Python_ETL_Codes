import pandas as pd 

'''
@Author: Matheus Barros
Date: 26/12/2020

'''

#========== GENERATING LIST OF COLUMNS NAME ==========

df_cols_name = pd.read_csv("movies_dataset.csv",nrows = 0)
lst_cols_name = list(df_cols_name)

#========== GENERATING DATAFRAME WITH THE FIRST 200 ROWS, PASSING AS ARGUMENT A LIST CONTAINING THE COLUMNS' NAME ==========
df_movies = pd.read_csv("movies_dataset.csv", 
                       	nrows = 200,
                       	skiprows = 100,
                       	header = None,
                       	names = lst_cols_name)

#========== PRINT THE FIRST 5 ROWS ==========
print(df_movies.head(5))


