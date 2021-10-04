from flask import Flask
from flask_restful import Resource, reqparse
import requests

# simple api endpoint to retrieve top 100 albums from Itune. endpoint = localserver/ituneAlbums or /ituneAlbums/limit=<limit>
# You can also pass on limit in the json body
# The method will get top n album depend on the parameter, default will be 100. 

class ituneAlbums(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('limit')
        args = parser.parse_args()
        limit = int(100)
        if args['limit']:
            limit = int(args['limit'])
        if limit > 100:
            return {'message': f'Number of album requested exceeds limit '}, 401
        response = requests.get(f'https://itunes.apple.com/us/rss/topalbums/limit={limit}/json')
        if response.status_code != 200:
            return {'message': f'Error connecting to Itune. Please try again later.'}, 501
        if (response.content):
            return  response.json(), 200
        else:
            return {'message': f'Albums not available at this moment. Please try again later'}, 400