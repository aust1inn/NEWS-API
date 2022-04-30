from flask import render_template,request,redirect,url_for

from . import main
from ..requests import get_source,get_headlines

@main.route('/')
def index():
    
    source =get_source()
    headline=get_headlines()
    return render_template('index.html',sources=source,headlines=headline)
