# forms.py
 
from wtforms import Form, StringField, SelectField
 
class BrokerSearchForm(Form):
    choices = [('Broker', 'Broker')]
    select = SelectField('Search for:', choices=choices)
    search = StringField('')
