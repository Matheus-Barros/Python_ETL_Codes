import pandas as pd

'''
@Author: Matheus Barros
Date: 17/12/2020

'''

try:
  #========== Set warn_bad_lines to issue warnings about bad records ==========
  data = pd.read_csv("movies_dataset_corrupted.csv", 
                     error_bad_lines = False, 
                     warn_bad_lines = True)
  
  #========== View first 5 records ==========
  print('\nDATAFRAME:\n',data.head(5))
  
except Exception as e:
    print('Erro found:',e)
