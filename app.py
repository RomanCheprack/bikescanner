from flask import Flask, request, render_template, url_for
from models import bike_discount, merlin_bikes

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
		return render_template('search.html', discount_res=discount_res, merlin_res=merlin_res)
	else:
		return render_template('search.html')


if __name__ == '__main__':
	app.run(debug=True)

