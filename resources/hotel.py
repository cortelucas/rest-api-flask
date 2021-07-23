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
    