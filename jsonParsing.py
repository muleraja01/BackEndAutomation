import json

courses='{"name" : "Raja Sekhar Reddy","languages": ["java","Python","UFT"]}'
#"Loads method parse json string and it reuturns dictionar"

dict_courses=json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
#get the first language of the experience
list_language=dict_courses['languages']
print(list_language[0])
