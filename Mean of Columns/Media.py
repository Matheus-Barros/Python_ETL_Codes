import pandas as pd
import numpy as np

'''
@Author: Matheus Barros
Date: 19/12/2020

'''


#========== GERANDO DATAFRAME ==========  
d = {'Filme':['Uma noite no museu','Watchmen','Click','Meu malvado favorito'] , 'Nota':[5,2,6,np.nan]}
df_filme = pd.DataFrame(data = d)

#========== SUBSTITUINDO CAMPOS NaN COM 8 ==========  
df_filme = df_filme.fillna({"Nota":8})
print(df_filme)

#========== TIRANDO A MÉDIA DAS NOTAS ==========  
Media_Filmes = str(df_filme.Nota.mean())

print('\nMédia das notas dos filmes listados :',Media_Filmes,'\n')

