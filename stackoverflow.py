import requests
from bs4 import BeautifulSoup
import json
q= requests.get('https://stackoverflow.com/questions/tagged/python')

som = BeautifulSoup(q.content , "html.parser")
#print(som)

#questions = som.select(".question-summary")

#print(questions[0].select_one('.question-hyperlink').getText())

convert = som.findAll('div', {'class': 'post-tag'})
#print(len(convert))

convert2 = som.findAll('div', class_ = 'summary')
one = []

for item in convert2:
    one.append({
    'title': item.find('a', class_ = 'question-hyperlink').getText(strip=True),
    'tag': item.find('a', class_ = 'post-tag').getText(strip=True),
    'link': item.find('a', class_ = 'question-hyperlink').get('href')
    })
for o in one:
    print(f"{o['title']} тэг {o['tag']} имеется, линка на запись https://stackoverflow.com/{o['link']}")
