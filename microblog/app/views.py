from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Zach'}
    posts = [ # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
            },
        {
            'author': {'nickname': 'Pablo' },
            'body': 'Luke, I am your father!'
            }
        ]
    return render_template('index.html', title='Home', user=user, posts=posts)
