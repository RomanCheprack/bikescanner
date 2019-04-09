from bs4 import BeautifulSoup as bs
import requests
import app


def bike_discount(search_term):
	l = []
	with requests.Session() as c:
		url = "https://www.bike-discount.de/en/search?currency=5&delivery_country=72"
		search_term = {'q': search_term}
		#c.get(url, params=search_term)
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
			#d['pro_desc'] = pro_desc
			d['link'] = link
			d['price'] = price
			l.append(d)
	l_sorted = sorted(l, key = lambda i: i['price']) 
	return l

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
			img = product.find("img")["src"]
			brand_name = product.find(class_="product-title").get_text().partition(' ')[0]
			brand_desc = product.find(class_="product-title").get_text().partition(' ')[2]
			price = product.find(class_="currencySymbol").get_text().partition('£')[2]
			link = product.find("a")["href"]
			d["img"] = img
			d["brand_name"] = brand_name
			d["brand_desc"] = brand_desc
			d["price"] = price
			d["link"] = link
			l.append(d)
	return l