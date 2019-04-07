from flask import Flask, request, render_template, url_for
from models import bike_discount, merlin_bikes

app = Flask(__name__)






@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		search_term = request.form['search_term']
		discount_res = bike_discount(search_term)
		merlin_res = merlin_bikes(search_term)
		displayed_url = displayed_url
		return render_template('home.html', discount_res=discount_res, merlin_res=merlin_res, displayed_url=displayed_url)
	else:
		return render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)