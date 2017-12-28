# Created by FelipeCRamos

'''

Esse programa foi criado pois, cada vez que eu desejava ver o preço de uma bike,
tinha que clicar na bike para então ver o preço, para fazer comparações isso é realmente imprático.

'''

import urllib.request
import re

website_link = 'http://groovebikes.com.br/produtos/'

class Bike:
	def __init__(self, name, link = '#', price = 0):
		self.name = name
		self.link = link
		self.price = price

bike_list = []

def obtainPrice(link):
	try:
		site = urllib.request.urlopen(link)
		site_data = str(site.read())
		price = re.findall(r'">R\$\s(.+?)</span>', site_data)
		conv = str(price[0]).replace('.', '')
		conv = int(conv)
		return conv

	except Exception as e:
		print("ERROR:", str(e))

def showResults(bike_list):
	for bike in bike_list:
		print("R$ {:>5},00 - {}".format(bike.price, bike.name))

website = urllib.request.urlopen(website_link)
website_data = str(website.read())

print("\n\nStarting to fetch prices from {}...\n\n".format(website_link))

links = re.findall(r'<a href="http://groovebikes\.com\.br/bike/.+?</a>', website_data)

for link in links:
	bike_link = re.findall(r'''href="(.+)">''', link)[0]
	bike_name = re.findall(r'''alt="(.+)"\ssrc''', link)[0]
	
	t_bike = Bike(name = bike_name, link = bike_link, price = obtainPrice(bike_link)) # t_bike stands for temporary bike.
	
	bike_list.append(t_bike)
	
	print("R$ {:>5},00 - {}".format(t_bike.price, t_bike.name))
	print("{}\n".format(t_bike.link))
	
	t_bike = None

print("\nDone.\n")