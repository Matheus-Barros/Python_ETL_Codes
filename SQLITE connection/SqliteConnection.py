import pandas as pd
from sqlalchemy import create_engine

'''
@Author: Matheus Barros 
Date: 27/12/2020

'''
try:
	#========== Create the database engine ==========
	engine = create_engine("sqlite:///cars.db")

	#========== Create a SQL query to load the entire weather table ==========
	query = """
	SELECT * 
	  FROM car;
	"""
	
	#OR
	
	query = 'SELECT * FROM car;'

	#========== Load weather with the SQL query ==========
	weather = pd.read_sql(query, engine)

	#========== View the first few rows of data ==========
	print(weather.head())

except Exception as e:
	print(e)
