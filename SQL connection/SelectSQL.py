import pandas as pd
import mysql.connector

'''
@Author: Matheus Barros
Date: 25/12/2020

'''
#========== GENERATING CONNECTION ==========  
connection = mysql.connector.connect(host = 'localhost',
									user = 'root',
									passwd = '',
									db = 'mysql')

#========== SELECTING DATABASE ==========  
data = pd.read_sql_query('SELECT * FROM db;',connection)

print(data)



