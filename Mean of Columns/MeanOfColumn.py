import pandas as pd
import numpy as np

'''
@Author: Matheus Barros
Date: 19/12/2020

'''

#========== GENERATING DATAFRAME ==========  
d = {'Filme':['Uma noite no museu','Watchmen','Click','Meu malvado favorito'] , 'Nota':[5,2,6,np.nan]}
df_filme = pd.DataFrame(data = d)


#========== MEAN OF GRADES ==========  
Media_Filmes = str(df_filme.Nota.mean())

print('\nMeans of movies :',Media_Filmes,'\n')

