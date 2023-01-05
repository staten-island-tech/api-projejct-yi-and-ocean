import os
import json
import requests
from flask import Flask, render_template, redirect, request
from flaskr.static.library.func import *
from flaskr.static.library.data import *


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('index.html', word=getWord(randomWord()))
    
    @app.route('/word', methods =["GET", "POST"])
    def word():
        word=request.form['searchForWord']
        if word:
            return redirect('/word/'+ word )
        else:
            return render_template('404.html')
    
    @app.route('/word/<path:search>', methods =["GET", "POST"])
    def search(search):
        result = getWord(search)
        return render_template(checkValidWord(result), word=result, types=typesOfWords())
    
    @app.route('/types', methods =["GET", "POST"])
    def types():
        wordType = request.form['typeSelector']
        return redirect ('/word/
    
    return app