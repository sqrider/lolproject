import requests

#Ask user for Summoner ID, and make API CALL #1 to determine Summoner ID

#Ask user for summoenr name input
summoner_name = raw_input('Enter summoner name:  ')

#make lowercase
summoner_name = summoner_name.lower()
#remove whitespaces
summoner_name = summoner_name.strip()

#Reduce to lowercase and concatenate to web_url
web_url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + summoner_name + '?api_key=149f0504-eace-4b70-abeb-99f0de4c2cdf'

requests_summoner = requests.get(web_url)

#built-in json decoder from Requests loads JSON
parsed_summoner = requests_summoner.json()

#retrieve summoner's ID number
summoner_id = parsed_summoner[summoner_name]["id"]

#print summoner ID for troubleshooting
print(summoner_id)
print(summoner_name)
