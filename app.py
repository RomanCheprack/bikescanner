from flask import Flask, request, render_template, url_for
from models import bike_discount, merlin_bikes
import csv

app = Flask(__name__)


@app.route("/", methods=['GET'])
@app.route("/home")
def home():
	return render_template('home.html')
	
@app.route("/search", methods=['GET', 'POST'])
def search():
	if request.method == 'POST':
		search_term = request.form['search_term']
		discount_res = bike_discount(search_term)
		merlin_res = merlin_bikes(search_term)
		with open('bike_discount.csv', 'r') as file:
			data = csv.DictReader(file)
			return render_template('search.html',search_term=search_term, data=data, merlin_res=merlin_res)
	else:
		return render_template('search.html')

@app.route("/price")
def price():
	pass
	


if __name__ == '__main__':
	app.run(debug=True)

