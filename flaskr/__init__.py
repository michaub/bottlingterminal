import os

from flask import Flask, render_template

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #Not sure if below will be right - check
        DATABASE=os.path.join(app.instance_path, 'postgreSQL'),
    )
    if test_config is None:
        #Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        #Load the test config if passed in
        app.config.from_mapping(test_config)

    #Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    #A simple page that says hello

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def index():
        return render_template("dashboard.html")

    return app