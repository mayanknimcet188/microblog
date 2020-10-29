from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Mayank'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username':'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author':{'username':'Mayank'},
            'body':'Hi this is my first post'
        }                                      
    ]                    
    return render_template('index.html',title='Home', user=user, posts=posts)
           
           
