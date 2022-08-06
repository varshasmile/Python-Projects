import requests
import re
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://www.ndtv.com/latest")
print(res)
# print(res.text)

soup = BeautifulSoup(res.text, "html.parser")
# print(soup)
# print(soup.body)
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all("a"))
# print(soup.title)
# print(soup.find("a"))
# print(soup.select(".cityname"))
# print(soup.select("h1"))
# print(soup.select("h2")[1])

links = soup.select(".newsHdng")
# print(links)

# for idx, item in enumerate(links):
# 	print(idx, item)

def create_custom_news(links):
	news = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].find('a', attrs={'href': re.compile("^https://")})
		href2 = href.get("href")
		news.append({"title" : title, "links" : href2})
	return news

todays_news = str(create_custom_news(links))

with open("todays_news.txt", mode = 'w') as my_file:
	text = my_file.write(todays_news)
	pprint.pprint(text)

