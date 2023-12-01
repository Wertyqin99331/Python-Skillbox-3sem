import requests
import json

url = 'https://swapi.dev/api/starships/10'
starship_data = requests.get(url).json()

pilots = []

for pilot in starship_data['pilots']:
	pilot_data = requests.get(pilot).json()
	homeworld_data = requests.get(pilot_data['homeworld']).json()

	pilot_info = {
		'height': pilot_data['height'],
		'homeworld': homeworld_data['name'],
		'homeworld_url': pilot_data['homeworld'],
		'mass': pilot_data['mass'],
		'name': pilot_data['name']
	}

	pilots.append(pilot_info)

ship_info = {
	'max_atmosphering_speed': starship_data['max_atmosphering_speed'],
	'pilots': pilots,
	'ship_name': starship_data['name'],
	'starship_class': starship_data['starship_class']
}

print(json.dumps(ship_info, indent=4))

with open('millennium_falcon.json', 'w') as f:
	json.dump(ship_info, f, indent=4)
