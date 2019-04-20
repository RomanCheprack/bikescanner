from bs4 import BeautifulSoup as bs
import csv
import requests
import app


def bike_discount(search_term):
	l = []
	with requests.Session() as c:
		url = "https://www.bike-discount.de/en/search?currency=5&delivery_country=72"
		search_term = {'q': search_term}
		res = c.post(url, params=search_term)
		soup = bs(res.text, "html.parser")
		products = soup.find_all(class_="uk-width-1-2 uk-width-medium-1-3")
		
		for card in products:
			d = { }
			pro_img = card.find("img")["data-src"]
			pro_desc = card.find("h3").get_text().replace(" ", "").replace("\n", "--")
			brand_name = pro_desc.split('--')[0]
			link = card.find("a")["href"]
			price = card.find(class_="price-value").get_text().replace("€", "").replace(" ", "")
			d['pro_img'] = pro_img
			d['brand_name'] = brand_name
			d['pro_desc'] = pro_desc
			d['link'] = link
			d['price'] = price
			l.append(d)
	#l_sorted = sorted(l, key = lambda i: i['price']) 
	keys = l[1].keys()
	with open('database.csv', 'w') as file:
		dict_writer = csv.DictWriter(file, keys)
		dict_writer.writeheader()
		dict_writer.writerows(l)

def merlin_bikes(search_term):
	with requests.Session() as r:
		l = []
		url = "https://bikes.merlincycles.com/search?"
		displayed_url = "www.merlincycles.com"
		search_term = {'w': search_term}
		res = r.post(url, params=search_term)
		soup = bs(res.text, "html.parser")
		all_products = soup.find_all(class_="product col-sm-4")

		for product in all_products:
			d = { }
			pro_img = product.find("img")["src"]
			pro_desc = product.find(class_="product-title").get_text().partition(' ')[2]
			brand_name = product.find(class_="product-title").get_text().partition(' ')[0]
			link = product.find("a")["href"]
			price = product.find(class_="currencySymbol").get_text().partition('£')[2]
			d["pro_img"] = pro_img
			d["brand_name"] = brand_name
			d["pro_desc"] = pro_desc
			d["link"] = link
			d["price"] = price
			l.append(d)
	
	keys = l[1].keys()
	with open('database.csv', 'a') as file:
		dict_writer = csv.DictWriter(file, keys)
		#dict_writer.writeheader()
		dict_writer.writerows(l)
	

def bike24(search_term):
	with requests.Session() as c:
		l = []
		url = "https://www.bike24.com/search?"
		search_term = {'searchTerm': search_term}
		res = c.post(url, params=search_term)
		soup = bs(res.text, "html.parser")
		products = soup.find_all(class_="col-xs-9 col-md-6")
				
		for card in products:
			d = { }
			pro_img = card.find("source")["srcset"].partition(' ')[0]
			pro_desc = card.find(class_="text-title")
			pro_desc = pro_desc.find('a')["title"]
		# 	brand_name = pro_desc.split('--')[0]
		# 	print(brand_name)
			link = card.find("a")["href"]
			price = card.find(class_="text-price").get_text().partition('*')[0]
			d['pro_img'] = pro_img
			d['brand_name'] = None
			d['pro_desc'] = pro_desc
			d['link'] = link
			d['price'] = price
			l.append(d)
	keys = l[1].keys()
	with open('database.csv', 'a') as file:
		dict_writer = csv.DictWriter(file, keys)
		#dict_writer.writeheader()
		dict_writer.writerows(l)