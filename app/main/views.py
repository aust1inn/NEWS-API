from flask import render_template,request,redirect,url_for

from . import main
from ..requests import get_source,get_headlines,article_source

@main.route('/')
def index():
    
    source =get_source()
    headline=get_headlines()
    return render_template('index.html',sources=source,headlines=headline)

@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    articles = article_source(id)
    return render_template('news.html',articles= articles,id=id )
