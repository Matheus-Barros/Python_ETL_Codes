'''
@Author: Matheus Barros
Date: 02/28/2021

'''
import json

data = {
    	"president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    		}
		}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)