import json

with open('Json/states.json') as f:
    data = json.load(f) # load a json object to a python dict

print(type(data))
for state in data['states']:
    del state['area_codes']

with open('Json/new_states.json','w') as f:
    json.dump(data,f,indent=2)
