import pandas as pd
import mysql.connector
import contextlib

'''
@Author: Matheus Barros
Date: 08/01/2021

'''

@contextlib.contextmanager
def query_database(query):

	#========== GENERATING CONNECTION ========== 
	print('**Conecting to Database')
	connection = mysql.connector.connect(host = 'localhost',
										user = 'root',
										passwd = '',
										db = 'mysql')

	#========== SELECTING DATABASE ==========
	print('****Quering Database')
	data = pd.read_sql_query(query,connection)
	
	yield data

	print('\n******Disconecting of Database******\n')
	connection.close()



query = 'SELECT * FROM db;'

with query_database(query) as my_db:
	print(my_db)