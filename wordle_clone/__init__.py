import os

from flask import Flask, session


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'wordle_clone.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
  
    @app.before_request
    def before_request():
        if 'solution_word' not in session:
            session['solution_word'] = 'idols'
            session['guessed_words'] = []

    from . import game_page
    app.register_blueprint(game_page.bp)

    @app.route("/hello")
    def hello_world():
        return "<p>Hello World<p>"
    
    return app