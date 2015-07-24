import requests
#import json
#from urllib2 import Request, urlopen, URLError
#
#web_api_request = Request("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/RiotSchmick?api_key=149f0504-eace-4b70-abeb-99f0de4c2cdf")
#
#try:
#    json_summoner = urlopen(web_api_request)
#    parsed_summoner = json_summoner.read()
#    print(parsed_summoner["riotschmick"]["id"])
#except URLError, e:
#    print("failure")

#make web api call w/ api key
request_summoner = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/ILoveWho?api_key=149f0504-eace-4b70-abeb-99f0de4c2cdf')

#built-in json decoder loads JSON
parsed_summoner = request_summoner.json()

#print Summoner id
print(parsed_summoner["ilovewho"]["id"])
