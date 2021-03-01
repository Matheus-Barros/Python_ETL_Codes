'''
@Author: Matheus Barros
Date: 02/28/2021

'''
import singer

json_schema = {
	"properties": {"age": {"maximum": 130,
							"minimum": 1,
							"type": "integer"},
					"has_children": {"type": "boolean"},
					"id": {"type": "integer"},
					"name": {"type": "string"}},
	"$id": "http://yourdomain.com/schemas/my_user_schema.json",
	"$schema": "http://json-schema.org/draft-07/schema#"}


schema = singer.write_schema(schema=json_schema,
					stream_name='DC_employees',
					key_properties=["id"])