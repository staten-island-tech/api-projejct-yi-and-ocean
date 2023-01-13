import os
import json
import requests
from flask import Flask, render_template, redirect, request, session
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
    
    @app.route('/search', methods =["GET", "POST"])
    def search():
        word=request.form['searchForWord']
        if word:
            return redirect('/search/'+ word )
        else:
            return render_template('404.html')
    
    @app.route('/search/<path:search>', methods =["GET", "POST"])
    def result(search):
        result = getWord(search)
        session['word'] = search
        args = request.args.to_dict()
        if args:
            wordType = args['type']
        else:
            wordType = None
        return render_template(checkValidWord(result), word=result, types=typesOfWords(), search=search.capitalize() , type = wordType)
    
    @app.route('/types', methods =["GET", "POST"])
    def types():
        wordType = request.form['typeSelector']
        word = session.get('word')
        return redirect ('/search/' + word + '?type=' + wordType)
    
    return app