# main.py
 
from app import app
from db_setup import init_db, db_session
from forms import BrokerSearchForm
from flask import flash, render_template, request, redirect
from models import Contact
 
init_db()
 
 
@app.route('/', methods=['GET', 'POST'])
def index():
    search = BrokerSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
 
    return render_template('index.html', form=search)
 
 
@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search.data['search'] == '':
        qry = db_session.query(Album)
        results = qry.all()
 
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0')
