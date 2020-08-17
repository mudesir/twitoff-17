from flask import Flask


def create_app():
    """ Create and Configure an instance of the app """
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Hello Twitoff!'
    return app


