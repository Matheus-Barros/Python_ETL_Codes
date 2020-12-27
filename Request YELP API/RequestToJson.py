import pandas as pd
import requests
import json

'''
@Author: Matheus Barros 
Date: 28/12/2020

'''
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

except Exception as e:
	print(e)
