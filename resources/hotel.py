from types import new_class
from flask_restful import Resource, reqparse
hoteis = [
  {
    'id': 'alpha',
    'name': 'Alpha Hotel',
    'stars': 4.3,
    'daily': 420.34,
    'city': 'Rio de Janeiro'
  },
  {
    'id': 'bravo',
    'name': 'Bravo Hotel',
    'stars': 4.4,
    'daily': 380.90,
    'city': 'Santa Catarina'
  },
  {
    'id': 'charlie',
    'name': 'Charlie Hotel',
    'stars': 4.3,
    'daily': 420.34,
    'city': 'São Salvador'
  },
]

class Hoteis(Resource):
  def get(self):
    return {'hoteis': hoteis}

class Hotel(Resource):

  def get(self, id):
    for hotel in hoteis:
      if hotel['id'] == id:
        return hotel
    return {'message': 'hotel não encontrado'}, 404 #not found
    
  def post(self, id):

    arguments = reqparse.RequestParser()

    arguments.add_argument('name')
    arguments.add_argument('stars')
    arguments.add_argument('daily')
    arguments.add_argument('city')

    data = arguments.parse_args()

    new_hotel = {
      "id": id,
      "name": data['name'],
      "stars":data['stars'],
      "daily":data['daily'],
      "city":data['city']
    }

    hoteis.append(new_hotel)

    return new_hotel, 200 #success