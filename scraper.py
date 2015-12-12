from bs4 import BeautifulSoup
import requests, time

f = open("C:/Users/vujke/Documents/GitHub/tech-job-market-rs/data/data.txt" ,"w")

url = "http://www.lisa.rs/slobodno-vreme/price-iz-srbije/10516-kalendar-poznatijih-srpskih-slava.html"

response = requests.get(url)

result = response.content

#make BeautifulSoup object
soup = BeautifulSoup(result, 'html.parser')

proba = soup.h3.get_text()
print proba
