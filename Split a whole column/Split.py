import pandas as pd

'''
@Author: Matheus Barros
Date: 17/12/2020

'''

#========== GERANDO DATAFRAME ==========  
d = {'email':['matheuspopx@gmail.com','biancapopx@outlook.com']}
df = pd.DataFrame(data = d)

#========== FAZENDO UMA COPIA DA COLUNA EMAIL E CONVERTENDO COLUNAS PARA STRING ========== 
df_col1 = df.email.astype(str)

#========== REALIZANDO O SPLIT E RETORNANDO UM NOVO DATAFRAME DIVIDIDO ========== 
df_col1 = df_col1.str.split('@',expand=True)

#========== CRIANDO NOVAS COLUNAS E SETANDO OS VALORES FILTRADOS ========== 
df = df.assign(nome = df_col1[0] , dominio= df_col1[1])

#========== IMPRIMINDO ========== 
print(df)
