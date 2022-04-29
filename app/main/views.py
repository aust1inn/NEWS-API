from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source,article_source

@main.route('/')
def index():
    
    source =get_source()
    return render_template('index.html',source=source)
