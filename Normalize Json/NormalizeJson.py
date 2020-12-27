import pandas as pd
import requests
import json
import warnings

# Load json_normalize()
from pandas.io.json import json_normalize

'''
@Author: Matheus Barros 
Date: 28/12/2020

'''
warnings.filterwarnings("ignore")

try:
	api_url = 'https://api.yelp.com/v3/businesses/search'

	#========== Get data about RJ cafes from the Yelp API ==========
	params = {"term":"bookstore",
			"location":"Rio de Janeiro"}

	api_key = 'jGw6fLMoQatH-bVyB_o3RrTfhCGrp5AlpfppURYfPb999erRjHWLhGI-3XDFsCFqQgLiNYranNF6ls5KZjYsoUmmqB2FfvkGCkmxcRizZomE0A2gjs6SCE7ArsPoX3Yx'

	headers = {"Authorization": "Bearer {}".format(api_key)}

	response = requests.get(api_url,
							params = params,
							headers = headers)


	#========== Extract JSON data from the response ==========
	data = response.json()

	#========== Load data to a data frame ==========
	bookstores = pd.DataFrame(data["businesses"])

	print(bookstores.head(5))

	#========== Flatten business data into a data frame, replace separator ==========
	cafes = json_normalize(data["businesses"],
                   			    sep="_")

	#========== Load other business attributes and set meta prefix ==========
	flat_cafes = json_normalize(data["businesses"],
	                            sep="_",
	                    		record_path="categories",
	                    		meta=['name', 
	                                  'alias',  
	                                  'rating',
	                          		  ['coordinates', 'latitude'], 
	                          		  ['coordinates', 'longitude']],
	                    		meta_prefix="biz_")

	print(flat_cafes)

except Exception as e:
	print(e)