from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(Form):
	search_term =  StringField('search', validators=[DataRequired])
	submit = SubmitField('Submit')