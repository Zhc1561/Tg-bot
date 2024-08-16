import requests
import json

x = 'class Math'
x = x.replace(' ','%20')
url = "https://api.stackexchange.com/2.3/search/advanced?order=desc&tagged=javascript&sort=relevance&q=%20"+x+"&site=stackoverflow"

response = requests.get(url)

data = json.loads(response.text)

questions = data["items"]
i = 0
for question in questions:
	if i < 3:
		print(question["title"],question["link"])
		i += 1