from flask import Flask
from flask_restful import Api
from src.api.albums import ituneAlbums

def create_app():
    """
    function that create flask application
    """
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(ituneAlbums, '/ituneAlbums', '/ituneAlbums/<limit>')
    return app

if __name__ == '__main__':
    app= create_app()
    app.run()