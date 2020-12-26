import pandas as pd

'''
@Author: Matheus Barros
Date: 17/12/2020

'''

#========== GENERATING DATAFRAME ==========  
d = {'email':['matheuspopx@gmail.com','biancapopx@outlook.com']}
df = pd.DataFrame(data = d)

#========== CONVERTING COLUMN TO STR ========== 
df_col1 = df.email.astype(str)

#========== SPLITING AND RETURNING A NEW DF ========== 
df_col1 = df_col1.str.split('@',expand=True)

#========== CREATING NEWS COLUMNS WITH THE VALUES SPLITED========== 
df = df.assign(nome = df_col1[0] , dominio= df_col1[1])

#========== PRINTING ========== 
print(df)
