import requests
import json


response_hulk = requests.get('https://superheroapi.com/api/2619421814940190/search/Hulk').text
hulk = json.loads(response_hulk)

response_cap = requests.get('https://superheroapi.com/api/2619421814940190/search/Captain America').text
cap = json.loads(response_cap)
#print(response_cap.text)

response_tha = requests.get('https://superheroapi.com/api/2619421814940190/search/Thanos').text
tha = json.loads(response_tha)
#print(hulk)
#print(cap['results'])
hulk_win = int(hulk['results'][0]['powerstats']['intelligence'])
cap_win = int(cap['results'][0]['powerstats']['intelligence'])
tha_win = int(tha['results'][0]['powerstats']['intelligence'])

who_win = [hulk_win, cap_win, tha_win]

if max(who_win) == hulk_win:
    print(f'самый умный Hulk ** {hulk_win} интелекта')
elif max(who_win) == cap_win:
    print(f'самый умный Captain America ** {cap_win} интелекта')
elif max(who_win) == tha_win:
    print(f'самый умный Thanos ** {tha_win} интелекта')
